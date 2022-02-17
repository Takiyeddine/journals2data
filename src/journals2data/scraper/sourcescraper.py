from typing import List, Any
from sklearn.metrics import precision_recall_fscore_support as score
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import pandas as pd
import requests, json, os
import os
import sys
import logging
import numpy as np 
import ast
from journals2data.data.mapurlinfo import MapURLInfo
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
from elasticsearch import Elasticsearch
es = Elasticsearch()
import journals2data
from journals2data import data
from journals2data import utils
from journals2data import console
from journals2data import exception
from journals2data.scraper import url_predict
from .articlescraper import ArticleScraper
from .scrapingresult import ScrapingResult, ScrapingResultFlag
from .mapurlarticlescraper import MapURLArticleScraper

class SourceScraper:

    source: data.Source
    config: journals2data.J2DConfiguration

    disappeard_urls_for_saving: data.MapURLInfo # URLs for saving
    known_article_url_for_rescraping: data.MapURLInfo # scrap to check if modified
    potential_article_urls_for_scraping: data.MapURLInfo # URLs to scrap this time
    raw_frontpage_urls: data.MapURLInfo
    #temporary variables
    ls_scores = [] 
    column_v =[]

    # object to keep between runs
    url_article_scrapers: MapURLArticleScraper # current and past article scrapers
    last_known_urls: data.MapURLInfo # URLs scraped from last scraping

    def __init__(
        self,
        source: data.Source,
        config: journals2data.J2DConfiguration
    ):  
        self.source = source
        self.config = config

        # default values    data.MapURLInfo({})
        self.last_known_urls = data.MapURLInfo()
        self.raw_frontpage_urls = data.MapURLInfo()
        self.disappeard_urls_for_saving = data.MapURLInfo()
        self.potential_article_urls_for_scraping = data.MapURLInfo()
        self.known_article_url_for_rescraping = data.MapURLInfo()

        # other defaults
        self.url_article_scrapers = MapURLArticleScraper()
    
    def scrap_all_urls(self):
        """
        Get all URLs from source:
        """

        # get URLs from source page
        self.raw_frontpage_urls = self.__get_all_website_links(
            self.source.url
        )

        # VERB: log self.raw_frontpage_urls size
        if(self.config.params["DEBUG"]):
            utils.log(
                self.config.params["VERBOSE"],
                "self.raw_frontpage_urls length after __get_all_website_links = " + \
                str(len(self.raw_frontpage_urls))
            )


    # web scraping functions
    def __get_all_website_links(
            self, url: str
        ) -> data.MapURLInfo:
        """
        Returns all URLs that is found on `url` in which it belongs 
        to the same website.
        """
        frontpage_urls: data.MapURLInfo = data.MapURLInfo()
        urls = set() # all URLs of `url`

        # domain name of the URL without the protocol
        domain_name = urlparse(url).netloc

        # get page raw html and check it worked
        if self.config.params["OFFLINE_P"] :
            page_raw_html: str = self.__get_page_raw_html_off_line(url)
        else:
            page_raw_html: str = self.__get_page_raw_html(url)
        if(page_raw_html == ""):
            # scraping failed, return empty data.MapURLInfo
            return frontpage_urls
        
        self.source.set_html(page_raw_html)
        
        # parse raw data with BeautifulSoup
        soup = BeautifulSoup(page_raw_html, "html.parser")

        # extract URLs and title info from related <a> tags
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            if parsed_href.query !='':
                href = parsed_href.scheme + "://" + \
                    parsed_href.netloc + parsed_href.path + \
                    '?'+ parsed_href.query 
            else:
                href = parsed_href.scheme + "://" + \
                    parsed_href.netloc + parsed_href.path

                    
            if not self.__is_valid(href):
                # not a valid URL 
                continue

            if href in frontpage_urls:
                # already in the set
                continue
            
            if domain_name not in href:
                # external link
                continue
            
            urls.add(href)
            
            raw_title: str = a_tag.getText().strip().lstrip()
            title: str = self.__clean_title_from_a_tag(raw_title)
            if title == "" or title is None:
                continue

            # build return object
            new_frontpage_url: data.FrontpageURLInfo = data.FrontpageURLInfo(
                url=href,
                title_from_a_tag=title
            )
            frontpage_urls[href] = new_frontpage_url

            if(self.config.params["VERBOSE"] == utils.VerboseLevel.NO_COLOR):
                print(str(new_frontpage_url))
            elif(self.config.params["VERBOSE"] == utils.VerboseLevel.COLOR):
                print(new_frontpage_url.to_str(pretty=False))

        return frontpage_urls
    
    def __is_valid(self, url: str):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)
    
    def __clean_title_from_a_tag(self, title: str) -> str:      
        title = title.replace(';','')
        title = title.replace('""','')
        title = title.replace("\n", "")
        title = title.replace("\t", "")
        return title
    
    def __get_page_raw_html(
        self, 
        url: str,
        is_browser_headless: bool = True,
        raw_html: str = ""
    ) -> str:
        """
        This function is used to scrap content from the front page
        of the Source using selenium.
        NOTE: It performs a down scrolling up to the bottom 
        of the page to make sure everything was scrapped.
        It returns None if the article is no more available online.
        TODO: change to async webdriver
        """
        
        # return directly if html was already provided
        if(raw_html != ""):
            return raw_html

        try:
            # open browser
            options = FirefoxOptions()
            options.add_argument("--headless")
            browser = webdriver.Firefox(options=options)
            
            # set timeout
            browser.set_page_load_timeout(
                self.config.params["ARTICLE_TIMEOUT"]
            )
            # get page and automatic scroll to bottom of page
            browser.get(url)
            browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            # get raw html
            raw_html = browser.page_source

        except TimeoutException as err:
            logging.exception(
                "TimeoutException with raw html scraping of the source [" +
                self.source.url + "] " +
                utils.get_str_time_now()
            )
            return ""

        except Exception as err:
            logging.exception(
                "Error with raw html scraping of the source [" +
                self.source.url + "] " +
                utils.get_str_time_now()
            )
            return ""

        finally:
            # close browser
            try:
                browser.close()
            except:
                pass
        
        return raw_html

    def __get_page_raw_html_off_line(
        self,
        url,

    ) -> str:
        domaine : str  = urlparse(url).netloc
        directory : str =  domaine
        parent_dir = self.config.params["HTML_FILES_PATH"]
        path_dir = os.path.join(parent_dir, directory)
        path_file = os.path.join(path_dir, "html"+".txt")
        with open(path_file) as f:
            contents = f.read()
        return contents

    def keep_known_urls(self):
        """
        Keep already known article URLs

            + 1) Iterate through keys (URL strings) of raw_frontpage_urls
            + 2) Check if they are present inside last_known_urls_map
            + 3) If present, add current pair to article_urls_for_scraping
        """

        # iterate through the dict keys: https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/ 
        urls_to_delete: List[str] = []
        for url in self.raw_frontpage_urls:
            # check if url key is present in self.last_known_urls
            if url in self.last_known_urls:
                # build list of urls to be able to remove them after
                # from self.last_known_urls
                # WARN: if deletion done while looping, can give error
                urls_to_delete.append(url)
                # copy pair to self.known_article_url_for_rescraping
                self.known_article_url_for_rescraping[
                    url] = self.raw_frontpage_urls[url]

        # remove recognized urls
        for url in urls_to_delete:
            del self.raw_frontpage_urls[url]
            # what remains will be saved after inside save_source_articles()
            del self.last_known_urls[url]
        
        # all recognised url have been deleted from self.last_known_urls
        # what remains is to be saved. 
        # WARN: Do a shallow copy
        self.disappeard_urls_for_saving = self.last_known_urls.copy()
        # WARN: Now that everything to be saved has been tranfered, clear
        self.last_known_urls.clear()

    def url_lifespan_check(self):
        """
        check lifespan of already known URLS
        If too long, act accordingly... ?
        remove them from potentially interesting URLs
        """
        # TODO: do something on self.known_article_urls_for_rescraping
        ...
    
    def save_source_articles(self):
        """
        Save articles whose URLs disappeared.
        NOTE: Remove their associated ArticleScraper from the list
        of current articles scraped.
        """

        # DBUG: KeyError. I want to see what's happening
        if(self.config.params["DEBUG"]):
            utils.log(
                self.config.params["VERBOSE"],
                "***** save_source_articles()",
                console.ANSIColorCode.LIGHT_ORANGE_C
            )

            keys_disappeard_urls_for_saving: list = list(
                self.disappeard_urls_for_saving.keys()
            )
            utils.log(
                self.config.params["VERBOSE"],
                "keys_disappeard_urls_for_saving = " + \
                str(keys_disappeard_urls_for_saving),
                console.ANSIColorCode.TURQUOISE_C
            )

            keys_url_article_scrapers: list = list(
                self.url_article_scrapers.keys()
            )
            utils.log(
                self.config.params["VERBOSE"],
                "keys_url_article_scrapers = " + \
                str(keys_url_article_scrapers),
                console.ANSIColorCode.LIGHT_BLUE_C
            )

        for url in self.disappeard_urls_for_saving:
            # remove article_scraper from self.url_article_scrapers
            # and save their corresponding articles
            # DBUG: KeyError, catch those errors
            try:
                article_scraper: ArticleScraper = self.url_article_scrapers.pop(url)
                article_scraper.save_article()
            except KeyError as err:
                utils.log(
                    self.config.params["VERBOSE"],
                    "KeyError detected [url: " + \
                    str(url) + "]",
                    console.ANSIColorCode.FAILED_C
                )
                print(err)
                continue
    
    def determine_article_urls(self):
        """
        Determine which ones are potential article URLs. 
        This is a crucial and heavy decision layer, using a range of 
        techniques such as BERT models, recurrence or heuristics for 
        decision-making.

        Objective of the function:
        Determine which URLs from self.raw_frontpage_urls are articles
        and pop them inside self.article_urls_for_scraping    
        """
        # TODO: finish method

        # convert raw_frontpage_urls.values: data.FrontpageURL to pd.DataFrame
        dframe: pd.DataFrame = self.raw_frontpage_urls.to_DataFrame()
        
        """
        dframe: pd.DataFrame = pd.DataFrame(data = {
            "url": [],
            "title_from_a_tag": [],
            "scraped_nb_times": []
        })
        """
        print("dframe = [see below] \r\n", dframe.head(20))

        # parse links through BERT, DOM and heuristics layers
        result_df: pd.DataFrame = self.__link_prediction_layers(dframe)
        print(
            "result_df after __link_prediction_layers= [see below] \r\n", 
            result_df.head(20)
        )

        # url for scraping selection decision based on previous results
        # adding relevant URL to the self.potential_article_urls_for_scraping
        def apply_url_selection(dataframe: pd.DataFrame) -> pd.DataFrame:

            def compute_prediction_score(row: pd.Series):
                # TODO: ameliorate ponderations depending on the key
                # FIXME: what does DOM layer for the score
                prediction_keys_with_ponderation: list = [
                    {"key": "BERT", "ponderation": 0.5},
                    {"key": "predicted_class", "ponderation": 0.5},
                    {"key": "h0", "ponderation": 0.7},
                    {"key": "h1", "ponderation": 0.7},
                    {"key": "h2", "ponderation": 1},
                    {"key": "h3", "ponderation": 1.3} 
                ]
                detection_sum: float = 0
                for element in prediction_keys_with_ponderation:
                    detection_sum += row[element["key"]]*element["ponderation"]

                return detection_sum

            dataframe["score"] = 0  # add column for results
            dataframe["score"] = dataframe.apply(
                compute_prediction_score, axis=1
            )

            return dataframe
        
        result_df = apply_url_selection(result_df)
        self.ls_scores = result_df.values.tolist()
        self.column_v = result_df.columns.values.tolist()
        print(
            "result_df after apply_url_selection = [see below]\r\n", 
            result_df.head(20)
        )

        def transfer_selected_url_for_scraping(row: pd.Series):
            # apply score threshold
            # TODO: ameliorate with decision tree
            if(row["score"] > 2.5):
                # transfer this URL for scraping
                url = row["URL"]
                if url in self.raw_frontpage_urls:
                    # transfer pair from raw to url for scraping
                    self.potential_article_urls_for_scraping[
                        url] = self.raw_frontpage_urls.pop(url)

        result_df.apply(transfer_selected_url_for_scraping, axis=1)


    def save_debug(self):
        """  
        this function will save the html page of each source with in a timestamp of scraping 
        it will also save the df that containe potentional article urls with BERT,H1,H2,H3,H4 scores.

        it will serve us to correct probleme of false positif and true negatif
        
         """

        domain_name: str  = urlparse(self.source.url).netloc
        timestamp: str = utils.get_str_time_now().replace(" ", "").replace("[","").replace("]","")[-19:]
        directory : str =  domain_name + timestamp
        parent_dir = "D:\PFE\Dev\Journal2data_off_line\out\debug_scores"
        path = os.path.join(parent_dir, directory)
        try:
            os.makedirs(path, exist_ok = True)
            print("Directory '%s' created successfully" % directory)
        except OSError as error:
            print("Directory '%s' can not be created" % directory)

        page_raw_html = self.__get_page_raw_html(self.source.url)
        dir_path = "D:\PFE\Dev\Journal2data_off_line\out\debug_scores/"+directory
        with open(os.path.join(dir_path,"html.txt"), 'w', encoding="utf-8") as file:
            file.write(page_raw_html)

        df_scores=pd.DataFrame(self.ls_scores)
        df_scores.columns = self.column_v
        df_scores['classe'] = np.where(df_scores['score'] > 2.5,1,0)

        df_scores.to_csv(os.path.join(dir_path,"url_automatic_selection.csv"),encoding='utf-8')


    def calculate_scores(self):
        df_scores=pd.DataFrame(self.ls_scores)
        df_scores.columns = self.column_v
        df_scores['classe'] = np.where(df_scores['score'] > 2.5,1,0)

        domain_name: str  = urlparse(self.source.url).netloc
        directory : str =  domain_name 
        parent_dir = "D:\PFE\Dev\Journal2data_off_line\out\debug_scores"
        path = os.path.join(parent_dir, directory)
        df_manual = pd.read_csv (os.path.join(path,"url_automatic_selection.csv"))

        

        predicted = df_manual['classe']
        manual = df_scores['classe']

        precision, recall, fscore, support = score(manual, predicted)

        print('precision: {}'.format(precision))
        print('recall: {}'.format(recall))
        print('fscore: {}'.format(fscore))
        print('support: {}'.format(support))


    def save_json_articles_to_elastic(self):
        es = Elasticsearch([self.source.params["ES_HOST"]],
                           http_auth=(self.source.params['ES_USER'], self.source.params['ES_PASSWORD']),
                           port=self.source.params['ES_PORT'])
        
        i : int = 1 
        index = self.source.params["ES_INDEX"]
        directory = self.source.params["ARTICLE_FILE_PATH"]
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                path_file = os.path.join(directory, filename)
                with open(path_file) as data_file:    
                    data = json.load(data_file)
                    for key in range(len(data)):
                        res = es.index(index=index, id=None, body=data[key])
                        i = i + 1 
                        print(res['result'])
                        print("\nSaved !!!!\n")
                

   
       



    def __link_prediction_layers(
        self, 
        title_link_df: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Apply BERT, DOM and the heuristic
        determination algorithms so as to get a multiple scores of 
        prediction for a link to be an article or not.
        """

        # pandas printing options
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        dframe = title_link_df.rename(columns={
            "url": "URL",
            "title_from_a_tag": "title",
            "scraped_nb_times": "scrap"
        })
        print("dframe base = [see below] \r\n", dframe.head(10))

        # WTCH: if source.html is empty, return
        if(self.source.html == None or self.source.html == ""):
            return dframe

            # VERB: log empty source!
            utils.log(
                self.config.params["VERBOSE"],
                "source.html [" + self.source.url + "] is empty.",
                console.ANSIColorCode.LIGHT_ORANGE_C
            )

        # [BERT] apply BERT prediction layer
        dframe = url_predict.apply_BERT_prediction(
            dframe, self.source, self.config
            )
        print("dframe columns = ", list(dframe))
        print(
            "dframe after apply_BERT_prediction = [see below] \r\n", 
            dframe.head(10)
        )

        # [DOM] apply DOM prediction layer
        dframe = url_predict.apply_DOM_prediction(
            dframe,
            self.source,
            self.config
        )
        print(
            "dframe after apply_DOM_prediction = [see below] \r\n", 
            dframe.head(10)
        )

        # [h0] apply 4 words on title heuristic 
        dframe = url_predict.apply_heuristic_h0(dframe)
        print(
            "dframe after apply_title_word_count_heuristic = [see below]\r\n", 
            dframe.head(20)
        )

        # [h1] apply h1 heuristic
        dframe = url_predict.apply_heuristic_h1(dframe)
        print(
            "dframe after apply_heuristic_h1 = [see below]\r\n", 
            dframe.head(20)
        )

        # [h2] apply h2 heuristic
        dframe = url_predict.apply_heuristic_h2(dframe)
        print(
            "dframe after apply_heuristic_h2 = [see below]\r\n", 
            dframe.head(20)
        )

        # [h3] apply h3 heuristic
        dframe = url_predict.apply_heuristic_h3(dframe)
        print(
            "dframe after apply_heuristic_h3 = [see below]\r\n", 
            dframe.head(20)
        )

        return dframe
        


    def scrap_known_url_articles(self):
        """
        Scrap URLs that have already been scraped in the passed and check
        if they were modified or not!
        """
        for url in self.known_article_url_for_rescraping:
            article_scraper: ArticleScraper = self.url_article_scrapers[url]
            # TODO: finish function
            # rescrap article and check if content was modified
            ...
    
    def scrap_new_potential_articles(self):
        """
        Scrap URLs that were not already known as articles but that
        have been marked as potential articles.
        Create an ArticleScraper for each of the URLs and launch 
        scraping process.
        NOTE: There is an evaluation of the article scraping score. 
        If too bad, the newly created ArticleScraper is not added to 
        self.url_article_scrapers.
        """ 

        # DBUG: limit number of potential articles to scrap
        __limit = self.config.params["POTENTIAL_ARTICLE_LIMIT"]
        if(__limit != None):
            tmp_transfer_dict = data.MapURLInfo()
            count: int = 0
            for url in self.potential_article_urls_for_scraping:
                if(count < __limit): 
                    tmp_transfer_dict[
                        url
                    ] = self.potential_article_urls_for_scraping[url]
                    count += 1
                else:
                    break
            self.potential_article_urls_for_scraping = tmp_transfer_dict
        
        # VERB: log nb of potential articles to scrap
        if(
            self.config.params["VERBOSE"].value == 
            utils.enums.VerboseLevel.COLOR
        ):
            console.println_ctrl_sequence(
                "*** nb of potential articles to scrap for source[" +
                self.source.url + "] = " + str(len(
                    self.potential_article_urls_for_scraping
                )),
                console.ANSICtrlSequence.PASSED
            )

        for url in self.potential_article_urls_for_scraping:
            article: data.Article = data.Article(
                self.source,
                url
            )
            article_scraper: ArticleScraper = ArticleScraper(
                article,
                self.config
            )

            # save article_scraper on scraping success
            scrap_result: ScrapingResult = article_scraper.scrap()
            if(scrap_result.flag == ScrapingResultFlag.SUCCESS):
                
                # log successful scraping
                if(self.config.params["VERBOSE"].value > 0):
                    article_scraper.log_successful_scraping()

                # save article_scraper if necessary
                def save_article_scraper():
                    # save article_scraper and url for future runs
                    self.url_article_scrapers[url] = article_scraper
                    self.last_known_urls[url] = self.potential_article_urls_for_scraping[url]

                    # increment scraping nb
                    self.last_known_urls[url].increment_scraped_nb()
                
                if(self.config.params["ARTICLE_SCORE_THRESHOLD"] == None):
                    save_article_scraper()
                # save if score > threshold
                elif(
                    self.config.params["ARTICLE_SCORE_THRESHOLD"] != None and
                    scrap_result.score >= self.config.params["ARTICLE_SCORE_THRESHOLD"]
                ):
                    save_article_scraper()
                else:
                    # VERB: log article_scaper and score
                    scrap_result.log_scraping_result(
                        "Warning: article_scraper not saved. Score too low."
                    )
            else:
                # VERB: log article_scaper and score
                scrap_result.log_scraping_result(
                    "Warning: article_scraper not saved. Scraping failed."
                )

    def save_all_now(self):
        """
        This method is used to save everything that need to be saved,
        for instance before terminating the run cicles.
        """

        # save all scraped articles
        for article_scraper in self.url_article_scrapers.values():
            article_scraper.save_article()

    def clean_ressources(self):
        """
        This method is used to clean ressources such as empty
        MapURLInfo object that need to be cleaned before
        next run.
        """
        self.disappeard_urls_for_saving = data.MapURLInfo()
        self.known_article_url_for_rescraping = data.MapURLInfo() 
        self.potential_article_urls_for_scraping = data.MapURLInfo()
        self.raw_frontpage_urls = data.MapURLInfo()

        # VERB: log self.raw_frontpage_urls size
        utils.log(
            self.config.params["VERBOSE"],
            "*** scraping run of source[" + \
            self.source.url + "] ended"
        )
        utils.log(
            self.config.params["VERBOSE"],
            "self.raw_frontpage_urls length = " + \
            str(len(self.raw_frontpage_urls))
        )










import typing
from typing import Union
import datetime
import re
import logging

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import newspaper
import unicodedata

import journals2data
from journals2data import data
from journals2data import utils
from .scrapingresult import ScrapingResult, ScrapingResultFlag

class ArticleScraper:

    config: journals2data.J2DConfiguration
    article: data.Article
    is_browser_headless: bool

    # flags
    rescraping: bool

    def __init__(
        self, 
        article: data.Article,
        config: journals2data.J2DConfiguration,
        is_browser_headless: bool = True
    ):
        self.article = article
        self.is_browser_headless = is_browser_headless
        self.config = config

        # default flag init
        self.rescraping = False

    def scrap(
        self, raw_html: str = "", rescrap: bool = False
    ) -> ScrapingResult:
        """
        This function is used to scrap content from the web
        of the Article using selenium.
        Optionally, the function can take direct raw html.
        It retuns itself if the scraping was successful.
        It returns None if the article is no more available online.
        TODO: change to async webdriver
        """
        # keep original full text for comparison
        if(rescrap and self.article.full_text != None):
            self.rescraping = True
            previous_full_text: str = str(self.article.full_text)
        
        try:
            # open browser
           # open browser
            options = FirefoxOptions()
            options.add_argument("--headless")
            browser = webdriver.Firefox(options=options)
            # set timeout
            browser.set_page_load_timeout(
                self.config.params["ARTICLE_TIMEOUT"]
            )

            # get raw html
            if(raw_html == "" or raw_html == "null"):
                self.article.raw_html = self.__get_article_raw_html(
                    browser
                )
            else:
                self.article.raw_html = raw_html

        except TimeoutException as e:
            logging.exception(
                "TimeoutException with raw html scraping of the article [" +
                self.article.url + "] " +
                utils.get_str_time_now()
            )
            return ScrapingResult(
                ScrapingResultFlag.RAW_SCRAPING_TIMEOUT,
                self.config
            )

        except Exception as Arguments:
            logging.exception(
                "Error with raw html scraping of the article [" +
                self.article.url + "] " +
                utils.get_str_time_now()
            )
            return ScrapingResult(
                ScrapingResultFlag.RAW_SCRAPING_FAILED,
                self.config
            )

        finally:
            # close browser
            try:
                browser.close()
            except:
                pass
        
        # extract content using newspaper from raw html
        self.__extract_data_from_raw_html()

        # if rescraping, compute relative difference
        if(self.rescraping):
            self.__compute_rescraping_relative_difference(
                previous_full_text
            )

        # evaluate scraping and parsing result
        self.__evaluate_scraping_and_parsing()

        return ScrapingResult(
            ScrapingResultFlag.SUCCESS,
            self.config
        )

        

    
    def __get_article_raw_html(self, browser: webdriver.Firefox) -> str:
        """
        Scrap raw html using selenium
        NOTE: can raise errors
        """
        raw_html: str = ""
        browser.get(self.article.url)
        raw_html = browser.page_source
        return raw_html

    def __extract_data_from_raw_html(self):
        """
        This method is used to retreive information from the 
        raw html using newspaper3k to self.article.
        WARN: do not confuse data.Article with newspaper.Article!
        """
        newspaper_article: newspaper.Article = newspaper.Article(
            self.article.url
        )
        # simulate download but by passing to it raw html instead
        newspaper_article.download(self.article.raw_html)

        def preprocess_raw_html(html_code: str) -> str:
            """
            Preprocess the html code by removing the "q" tag 
            and all tags about any table.
            """
            html_code = html_code.replace("<q>", '')
            html_code = html_code.replace("</q>", '')
            html_code = html_code.replace("</table>", '')
            html_code = html_code.replace("<tbody>", '')
            html_code = html_code.replace("</tbody>", '')
            html_code = html_code.replace("</tr>", '')
            html_code = html_code.replace("</td>", '')

            regextable = r"<table(.*?)>"
            regextr = r"<tr(.*?)>"
            regextd = r"<td(.*?)>"
            subst = "/n"
            html_code = re.sub(
                regextable, subst, html_code, 0, re.MULTILINE)
            html_code = re.sub(
                regextd, subst, html_code, 0, re.MULTILINE)
            html_code = re.sub(
                regextr, subst, html_code, 0, re.MULTILINE)
            return html_code

        newspaper_article.html = preprocess_raw_html(
            newspaper_article.html
        )

        # newspaper3k parsing
        newspaper_article.parse()

        # full text cleaning
        article_text = newspaper_article.text
        text = unicodedata.normalize(
            'NFKC', article_text).encode('utf-8', 'ignore')
        article_text = text.decode("utf-8")

        def replace_parenthesis(text: str) -> str:
            return text.replace('"', "'")

        #article_text = replace_parenthesis(article_text)
        self.article.set_full_text(article_text)

        # add last data from newspaper_article to article
        if(newspaper_article.title != None):
            self.article.title_from_page = replace_parenthesis(
                newspaper_article.title
            )
        if(newspaper_article.publish_date != None):
            self.article.publish_date = replace_parenthesis(
                str(newspaper_article.publish_date)
            )

        # log first scraping instant as self.timestamp_start
        if(
            self.article.timestamp_start == None or
            self.article.timestamp_start == ""
        ):
            self.article.timestamp_start = datetime.datetime.now().strftime(
                "%S_%M_%H_%d_%m_%Y"
            )
        self.article.timestamp_scraping = datetime.datetime.now().strftime(
               "%Y/%m/%d %H:%M:%S")
        

    def __compute_rescraping_relative_difference(
        self, previous_full_text: str
    ):
        ...


    def __evaluate_scraping_and_parsing(self):
        ...
    
    def log_successful_scraping(self):
        """
        VERB: display a part of the scraped full text. 
        This is a quick way to see what happened with
        the scraping of the article.
        """
        text_preview = utils.limit_line_str(
            self.article.full_text
        )
        url_preview = utils.limit_line_str(
            self.article.url
        )
        print(
            "Article scraped: " + 
            "[url: " + url_preview + "] " +
            "[txt: " + text_preview + "] " +
            utils.get_str_time_now()
        )
    
    def save_article(self):
        """
        This method is used to save all pending articles that 
        have already been scraped at least once.
        """
        self.article.save()
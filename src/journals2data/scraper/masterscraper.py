from typing import List
import time
import schedule

from journals2data import data
from journals2data import utils
from journals2data import exception
from journals2data import console
from journals2data import J2DConfiguration
from .sourcescraper import SourceScraper

class MasterScraper:

    sources: List[data.Source]
    source_scrapers: List[SourceScraper]
    config: J2DConfiguration

    def __init__(
        self, 
        config: J2DConfiguration
    ):
        if not isinstance(config, J2DConfiguration):
            raise ValueError(
                "Error: config is not a J2DConfiguration."
            )
        self.config = config
        
        # get sources
        self.sources = config.get_sources()
        if(len(self.sources) <= 0):
            raise exception.NoSourcesError(
                """
                Error: No sources were found.
                Nothing to do. Terminating.
                """
            )
        
        # create source scrapers
        self.source_scrapers = []
        for source in self.sources:
            source_scraper: SourceScraper = SourceScraper(
                source, config
            )
            self.source_scrapers.append(source_scraper)


    def scrap(self):
        """
        For each source in parallel:
            + 1) get all URLs from source
                    + source_scraper.scrap_all_urls()
            + 2) keep already known article URLs, 
                    + source_scraper.keep_known_urls()
            BONUS: check lifespan of already known URLS
            If too long, act accordingly... ?
            remove them from potentially interesting URLs
                    TODO: not implemented
                    + source_scraper.url_lifespan_check()
            + 3) save articles whose URLs disappeared
                    + source_scraper.save_source_articles()
            + 4) determine which ones are potential article URLs
                    + source_scraper.determine_article_urls()
            + 5) scrap already known URLs and check if content was modified
                    TODO: to be finished, crucial
                    + source_scraper.scrap_known_url_articles()
            + 6) scrap new potential Articles
            and evaluate scraping of URLs (entropy/confidence score)
                    TODO: to be finished, evaluation not implemented
                    + source_scraper.scrap_new_potential_articles()
            + 7) Clean dictionnaries and prepare next scraping run
                    + source_scraper.clean_ressources()

            FIXME: Not async, needed for schedule and improved performance
        """

        # sources scraping loop 
        for source_scraper in self.source_scrapers:
             #use a SourceScraper object to scrap URLs
             #TODO:    +1) multithread this loop
             #TODO:    +2) add scheduling method there
             '''
             source_scraper.scrap_all_urls()
             source_scraper.keep_known_urls()
             source_scraper.url_lifespan_check()
             source_scraper.save_source_articles()
             source_scraper.determine_article_urls()
             source_scraper.scrap_known_url_articles()
             source_scraper.scrap_new_potential_articles()
             source_scraper.clean_ressources()
             '''
             source_scraper.scrap_all_urls()
             source_scraper.determine_article_urls()
             source_scraper.calculate_scores()
             #source_scraper.save_json_articles_to_elastic()
        # run limit and saving
        self.config.params["RUN_NUMBER"] += 1
        if(self.config.params["NB_RUN_LIMIT"] != None):
            if( 
                self.config.params["RUN_NUMBER"] >= 
                self.config.params["NB_RUN_LIMIT"]
            ):  
                # change IS_J2D_RUNNING to false
                self.config.params["IS_J2D_RUNNING"] = False

                # saving pending scraped articles
                if(
                    self.config.params["VERBOSE"] == 
                    utils.VerboseLevel.COLOR
                ):
                    console.println_ctrl_sequence(
                        "****** RUN_NUMBER at maximum. Saving everything.",
                        console.ANSICtrlSequence.PASSED
                    )
                    self.save()
    
    def save(self):
        """
        Save everithing that needs to be saved.
        """
        for source_scraper in self.source_scrapers:
                source_scraper.save_all_now()

    def scheduled_sync_scrap(self):
        """
        This method calls the self.scrap() method 
        every SCHEDULE_SYNC_SCRAP_MIN minutes.
        NOTE: The SCHEDULE_SYNC_SCRAP_MIN conf param
        need to be defined and not equals to None.
        """

        def job(log_waiting_time: bool = False):
            # count job execution time
            job_start_time = time.time()

            # run main job
            self.scrap()

            # log job time
            job_execution_time = (time.time() - job_start_time)
            utils.log(
                self.config.params["VERBOSE"],
                "Scrap time for last run: " + str(job_execution_time),
                console.ANSIColorCode.LIGHT_ORANGE_C
            )

            # log waiting time if needed
            if(log_waiting_time):
                log_text: str = "... waiting for " + \
                    str(self.config.params[
                        "SCHEDULE_SYNC_SCRAP_MIN"
                    ]) + " minute(s)..."
                utils.log(self.config.params["VERBOSE"], log_text)

        if(
            self.config.params["SCHEDULE_SYNC_SCRAP_MIN"] != None and
            self.config.params["SCHEDULE_SYNC_SCRAP_MIN"] > 0
        ):
            interval: int = self.config.params[
                "SCHEDULE_SYNC_SCRAP_MIN"
            ]

            # run first time
            job(log_waiting_time=True)

            # run on schedule
            schedule.every(interval).minutes.do(
                job, log_waiting_time=True
            )
            while(self.config.params["IS_J2D_RUNNING"] == True):
                schedule.run_pending()
                time.sleep(1)
        else:
            job()

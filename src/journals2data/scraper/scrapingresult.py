from enum import IntEnum

import journals2data
from journals2data import console
from journals2data import utils

class ScrapingResultFlag(IntEnum):

    SUCCESS = 0
    RAW_SCRAPING_TIMEOUT = 1
    RAW_SCRAPING_FAILED = 2

class ScrapingResult():

    config: journals2data.J2DConfiguration

    flag: ScrapingResultFlag
    score: float

    def __init__(
        self, 
        result_flag, 
        config: journals2data.J2DConfiguration,
        score: float = 0
    ):
        """
        This is a return object for the ArticleScraper.scrap()
        method. It contains a ScrapingResultFlag and a score.
        NOTE: In case of error, score == 0.
        """
        self.flag = result_flag
        self.config = config
        self.score = score
    
    def __str__(self) -> str:
        string: str = "ScrapingResult[flag: "
        if(self.flag == ScrapingResultFlag.SUCCESS):
            string += "SUCCESS"
        elif(self.flag == ScrapingResultFlag.RAW_SCRAPING_TIMEOUT):
            string += "RAW_SCRAPING_TIMEOUT"
        elif():
            string += "RAW_SCRAPING_FAILED"
        else:
            string += "Error: no such enum value!"
        string += ", score: " + str(self.score) + "]" 
        return string
    
    def log_scraping_result(self, message: str = ""):
        """
        This method is used to log a ScrapingResult object
        to the console. Can print a message just before it.
        """
        if(
            self.config.params["VERBOSE"].value == 
            utils.enums.VerboseLevel.COLOR
        ):
            console.println_ctrl_sequence(
                message + str(self),
                console.ANSICtrlSequence.FAILED
            )
        elif(
            self.config.params["VERBOSE"].value == 
            utils.enums.VerboseLevel.NO_COLOR
        ):
            print(message + str(self))
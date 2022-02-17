from signal import signal, SIGINT
from sys import exit
from typing import Callable

from .configuration import J2DConfiguration
from journals2data import console
from journals2data import utils
from journals2data import scraper


class SignalHandler:

    config: J2DConfiguration
    master_scraper: scraper.MasterScraper

    def __init__(self, master_scraper: scraper.MasterScraper):
        """
        Modify signal handlers of the program.
        """
        self.master_scraper = master_scraper
        self.config = master_scraper.config

        # SIGINT
        self.__set_SIGINT_handling()
        
    
    def __set_SIGINT_handling(self):
        """
        Set a handler for SIGINT.
        """

        def SIGINT_handler(signal_received, frame):
            """
            Handle SIGINT program termination. Handle any cleanup here.
            Make sure scraped articles are correctly saved.
            """
            utils.log(
                self.config.params["VERBOSE"],
                "!!!!!! SIGINT or CTRL-C detected. Trying to exit gracefully !!!!!!",
                console.ANSIColorCode.RED_C
            )

            # perform exit tasks
            # 2FIX: not sure at all it will work ?!
            self.master_scraper.save()

            exit(0)
        
        # set handler
        signal(SIGINT, SIGINT_handler)

        # VERB: log signal set up
        utils.log(
            self.config.params["VERBOSE"],
            "****** SIGINT (CTRL + C) termination handled. ******",
            console.ANSIColorCode.LIGHT_BLUE_C
        )
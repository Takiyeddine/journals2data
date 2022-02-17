# this is the main object to run the library whithout dealing with
# internal objects  
import typing

from journals2data import data
from journals2data import utils
from journals2data import scraper
from journals2data import exception
from journals2data import console
from .configuration import J2DConfiguration
from .signalhandler import SignalHandler

class Journals2Data:

    config: J2DConfiguration
    master_scraper: scraper.MasterScraper
    signal_handler: SignalHandler

    def __init__(
        self, 
        journals2data_conf_filepath: typing.Optional[str]=None,
        config: typing.Optional[J2DConfiguration]=None
    ):  
        """
        Journals2Data main object.
        Can be instantiated either by giving the filepath to
        a conf file, or by directly providing a J2DConfiguration
        object.
        NOTE: At least one of the two option is required.
        INFO: If two optional params are given, only config
        will be considered.
        """

        # create config
        if(
            journals2data_conf_filepath == None and
            config == None
        ):
            raise ValueError(
                """
                Error: Both journals2data_conf_filepath and
                config are equal to None. Please provide one
                of the these parameters.
                """
            )
        elif(config != None):
            if not isinstance(config, J2DConfiguration):
                raise ValueError(
                    "Error: config is not a J2DConfiguration."
                )
            else:
                self.config = config
        else:
            self.config = J2DConfiguration(
                str(journals2data_conf_filepath)
            )
        
        # create master scraper
        self.master_scraper = scraper.MasterScraper (
            self.config
        )

        # create signal handler
        self.signal_handler = SignalHandler(
            self.master_scraper
        )

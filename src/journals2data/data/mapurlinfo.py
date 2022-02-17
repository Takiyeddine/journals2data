from journals2data import data
from .frontpageurlinfo import FrontpageURLInfo

import typing
from typing import Dict

import pandas as pd

typing.NewType('MapURLInfo', Dict[str, FrontpageURLInfo])

class MapURLInfo(dict):

    def __init__(self):
        """
        This type represents a mapping of key:value pairs
        between a URL string as key and a FrontpageURL as value.
        The idea is to be able to check at no cost that a specific
        URL string is present inside or not, and if so, to be able
        to retreive its informations contained inside a 
        FrontpageURL object at no cost.
        """
        self = dict()

    def to_DataFrame(self) -> pd.DataFrame:
            dframe: pd.DataFrame = pd.DataFrame(data = {
                "url": [],
                "title_from_a_tag": [],
                "scraped_nb_times": []
            })

            for frontpage_url in self.values():
                new_df_row = {
                    "url": frontpage_url.url,
                    "title_from_a_tag": frontpage_url.title_from_a_tag,
                    "scraped_nb_times": frontpage_url.scraped_nb_times
                }
                dframe = dframe.append(new_df_row, ignore_index=True)
            
            return dframe

from .articlescraper import ArticleScraper

import typing
from typing import Dict

typing.NewType('MapURLArticleScraper', Dict[str, ArticleScraper])

class MapURLArticleScraper(dict):

    def __init__(self):
        """
        This type represents a mapping of key:value pairs
        between a URL string as key and an ArticleScraper as value.
        The idea is to be able to check at no cost that a specific
        URL string is present inside or not, and if so, to be able
        to retreive its ArticleScraper (hence its Article) at no cost.
        """
        self = dict()
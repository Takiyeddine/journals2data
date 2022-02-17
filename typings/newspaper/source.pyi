"""
This type stub file was generated by pyright.
"""

"""
Source objects abstract online news source websites & domains.
www.cnn.com would be its own source.
"""
__title__ = ...
__author__ = ...
__license__ = ...
__copyright__ = ...
log = ...
class Category:
    def __init__(self, url) -> None:
        ...
    


class Feed:
    def __init__(self, url) -> None:
        ...
    


NUM_THREADS_PER_SOURCE_WARN_LIMIT = ...
class Source:
    """Sources are abstractions of online news vendors like huffpost or cnn.
    domain     =  'www.cnn.com'
    scheme     =  'http'
    categories =  ['http://cnn.com/world', 'http://money.cnn.com']
    feeds      =  ['http://cnn.com/rss.atom', ..]
    articles   =  [<article obj>, <article obj>, ..]
    brand      =  'cnn'
    """
    def __init__(self, url, config=..., **kwargs) -> None:
        """The config object for this source will be passed into all of this
        source's children articles unless specified otherwise or re-set.
        """
        ...
    
    def build(self): # -> None:
        """Encapsulates download and basic parsing with lxml. May be a
        good idea to split this into download() and parse() methods.
        """
        ...
    
    def purge_articles(self, reason, articles):
        """Delete rejected articles, if there is an articles param,
        purge from there, otherwise purge from source instance.

        Reference this StackOverflow post for some of the wonky
        syntax below:
        http://stackoverflow.com/questions/1207406/remove-items-from-a-
        list-while-iterating-in-python
        """
        ...
    
    def set_categories(self): # -> None:
        ...
    
    def set_feeds(self): # -> None:
        """Don't need to cache getting feed urls, it's almost
        instant with xpath
        """
        ...
    
    def set_description(self): # -> None:
        """Sets a blurb for this source, for now we just query the
        desc html attribute
        """
        ...
    
    def download(self): # -> None:
        """Downloads html of source
        """
        ...
    
    def download_categories(self): # -> None:
        """Download all category html, can use mthreading
        """
        ...
    
    def download_feeds(self): # -> None:
        """Download all feed html, can use mthreading
        """
        ...
    
    def parse(self): # -> None:
        """Sets the lxml root, also sets lxml roots of all
        children links, also sets description
        """
        ...
    
    def parse_categories(self): # -> None:
        """Parse out the lxml root in each category
        """
        ...
    
    def parse_feeds(self): # -> None:
        """Add titles to feeds
        """
        ...
    
    def feeds_to_articles(self): # -> list[Unknown]:
        """Returns articles given the url of a feed
        """
        ...
    
    def categories_to_articles(self): # -> list[Unknown]:
        """Takes the categories, splays them into a big list of urls and churns
        the articles out of each url with the url_to_article method
        """
        ...
    
    def generate_articles(self, limit=...): # -> None:
        """Saves all current articles of news source, filter out bad urls
        """
        ...
    
    def download_articles(self, threads=...): # -> None:
        """Downloads all articles attached to self
        """
        ...
    
    def parse_articles(self): # -> None:
        """Parse all articles, delete if too small
        """
        ...
    
    def size(self): # -> int:
        """Number of articles linked to this news source
        """
        ...
    
    def clean_memo_cache(self): # -> None:
        """Clears the memoization cache for this specific news domain
        """
        ...
    
    def feed_urls(self): # -> list[Unknown | str]:
        """Returns a list of feed urls
        """
        ...
    
    def category_urls(self): # -> list[Unknown | str]:
        """Returns a list of category urls
        """
        ...
    
    def article_urls(self): # -> list[Unknown]:
        """Returns a list of article urls
        """
        ...
    
    def print_summary(self): # -> None:
        """Prints out a summary of the data in our source instance
        """
        ...
    



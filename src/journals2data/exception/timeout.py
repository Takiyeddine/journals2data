class Timeout(Exception):
    """
    Base class for timeout exceptions.
    """
    pass

class FrontpageURLScrapingTimeout(Timeout):
    """
    The scraping process of the URLs of a source frontpage has
    reached timeout limit.
    """
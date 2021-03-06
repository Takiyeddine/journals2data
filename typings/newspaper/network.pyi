"""
This type stub file was generated by pyright.
"""

"""
All code involving requests and responses over the http network
must be abstracted in this file.
"""
__title__ = ...
__author__ = ...
__license__ = ...
__copyright__ = ...
log = ...
FAIL_ENCODING = ...
def get_request_kwargs(timeout, useragent, proxies, headers): # -> dict[str, Unknown | dict[str, Unknown] | CookieJar | bool]:
    """This Wrapper method exists b/c some values in req_kwargs dict
    are methods which need to be called every time we make a request
    """
    ...

def get_html(url, config=..., response=...): # -> str | bytes:
    """HTTP response code agnostic
    """
    ...

def get_html_2XX_only(url, config=..., response=...): # -> str | bytes:
    """Consolidated logic for http requests from newspaper. We handle error cases:
    - Attempt to find encoding of the html by using HTTP header. Fallback to
      'ISO-8859-1' if not provided.
    - Error out if a non 2XX HTTP response code is returned.
    """
    ...

class MRequest:
    """Wrapper for request object for multithreading. If the domain we are
    crawling is under heavy load, the self.resp will be left as None.
    If this is the case, we still want to report the url which has failed
    so (perhaps) we can try again later.
    """
    def __init__(self, url, config=...) -> None:
        ...
    
    def send(self): # -> None:
        ...
    


def multithread_request(urls, config=...): # -> list[Unknown]:
    """Request multiple urls via mthreading, order of urls & requests is stable
    returns same requests but with response variables filled.
    """
    ...


class Error(Exception):
    """
    Base class for other exceptions
    """
    pass

class NoSourcesError(Error):
    """
    Error raised when data.Source objects are expected but none
    is found in a collection like a List[data.Source].
    """
    pass

# class for global variables and parameters
# WARN: apparently, "global.py" is a bad name for a file

from enum import IntEnum

class VerboseLevel(IntEnum):
    """
    This enum is used for a better granularity
    on verbosity.
    NOTE: Use IntEnum instead of Enum fo correct 
    JSON serialization.
    WARN: Since it is an IntEnum, it is used as a value!
    """

    NONE = 0
    NO_COLOR = 1
    COLOR = 2

class ArticleSavingOption(IntEnum):
    """
    This enum presents the different options for saving the result
    from scraping of the obtained articles.
    WARN: Since it is an IntEnum, it is used as a value!
    """
    NO_SAVING = 0
    SAVE_TO_FILE = 1
    SAVE_TO_ELASTICSEARCH = 2
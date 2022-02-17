from journals2data import console

from .enums import VerboseLevel


def log(
    verbose_level: VerboseLevel,
    message: str,
    colorCode: console.ANSIColorCode = console.ANSIColorCode.DEBUG_C
):
    """
    This function logs message in color if possible, without color 
    if needed and noting if necessary, depending on the VERBOSE
    conf param.
    """
    # WARN: Can't use config object due to circular import
    if(verbose_level == VerboseLevel.NO_COLOR):
        print(message)
    elif(verbose_level == VerboseLevel.COLOR):
        console.println_fg_color(
            message,
            colorCode
        )
from typing import Union

from .ansicolorcode import ANSIColorCode
from .ansistring import ANSIString
from .ansictrlsequence import ANSICtrlSequence

# python enum : https://docs.python.org/3/library/enum.html 
# python typing : https://docs.python.org/3/library/typing.html 

def println_fg_color(
    message: str, colorCode: ANSIColorCode
) -> None:
    ctrlSequence: str = "%s%s%sm" % (
        ANSIString.ESC.value,
        ANSIString.FG_256.value,
        colorCode.value
    )
    print("%s%s%s" % (
        ctrlSequence,
        message,
        ANSICtrlSequence.RESET.value
    ))

def println_debug(message: str) -> None:
    println_fg_color(message, ANSIColorCode.DEBUG_C)

def println_ctrl_sequence(
    message: str, ctrlSequence: Union[ANSICtrlSequence, str]
) -> None:
    """
    This function is use with terminals to print the message
    with colors specified by an ANSI control sequence that 
    can be either a str or a console.ANSICtrlSequence object.
    """
    #print("type ctrlSequence = ", type(ctrlSequence))
    #if type(ctrlSequence) == ANSICtrlSequence:
    if isinstance(ctrlSequence, ANSICtrlSequence):
        ctrlSequenceStr: str = ctrlSequence.value
    else:
        ctrlSequenceStr = ctrlSequence
    
    print("%s%s%s" % (
        ctrlSequenceStr,
        message,
        ANSICtrlSequence.RESET.value
    ))

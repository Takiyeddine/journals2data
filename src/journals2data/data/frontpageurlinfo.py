import typing
from typing import Dict

import json

from journals2data import console

class FrontpageURLInfo:

    url: str
    title_from_a_tag: str
    scraped_nb_times: int

    def __init__(
        self,
        url: str,
        title_from_a_tag: str
    ):
        """
        Object that contains the information around a URL 
        obtained from scraping a source frontpage.
        """
        self.url = url
        self.title_from_a_tag = title_from_a_tag

        # default init values
        self.scraped_nb_times = 0
    
    def increment_scraped_nb(self):
        self.scraped_nb_times += 1
    
    def __str__(self) -> str:
        return self.to_str(
            pretty = False, 
            colors = False
        )
    
    # dict convertion: https://stackoverflow.com/questions/35282222/in-python-how-do-i-cast-a-class-object-to-a-dict/35282286#35282286 
    def to_dict(self) -> Dict[str, str]:
        json_str: str = str(self)
        return json.loads(json_str)
    
    def to_str(
        self, 
        pretty: bool = True, 
        nb_spaces: int = 4, 
        colors: bool = True
    ) -> str:
        """
        This function is use to produce a string from the object, 
        but contrary to __str__(self), this one can also produce
        pretty strings in a JSON-like serialization style.
        Supports colors in ANSI/VT100 format.
        """
        # pretty print in JSON-like serialization style
        endl: str = ""
        if(pretty):
            endl = "\r\n"

        spaces: str = ""
        if(pretty):
            # _ stands for unused variable
            #    + StackOverflow: https://stackoverflow.com/questions/5477134/how-can-i-get-around-declaring-an-unused-variable-in-a-for-loop 
            for _ in range(nb_spaces):
                spaces += " "
        
        # color support for terminals
        reset: str = ""
        key_color: str = ""
        value_color: str = ""
        if(colors):
            reset: str = console.ANSICtrlSequence.RESET.value
            key_color: str = "%s%s%sm" % (
                console.ANSIString.ESC.value,
                console.ANSIString.FG_256.value,
                console.ANSIColorCode.KEY_C.value
            )
            value_color: str = "%s%s%sm" % (
                console.ANSIString.ESC.value,
                console.ANSIString.FG_256.value,
                console.ANSIColorCode.VALUE_C.value
            )
        
        def __pretty_color_line(
            text: str, value: str, end_comma: str = ", "
        ) -> str:
            """
            Internal function to display a line of the serialisez 
            object. Needs to be declare inside "to_str" so as not
            to pass dozens of parameters which would cancel
            the pros of using a function here.
            """
            # standardize behaviour around None / empty str
            #    + GeekForGeeks: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/ 
            if(value == "None" or value == "" or value == None):
                value = "null"
            
            line: str = "%s%s\"%s\"%s: %s\"%s\"%s%s%s" % (
                spaces,
                key_color,
                text,
                reset,
                value_color,
                value,
                reset,
                end_comma,
                endl
            )
            return line
        
        to_string: str = ""
        to_string += "{" + endl
        to_string += __pretty_color_line(
            "url", str(self.url)
        )
        to_string += __pretty_color_line(
            "title_from_a_tag", str(self.title_from_a_tag)
        )
        to_string += __pretty_color_line(
            "scraped_nb_times", str(self.scraped_nb_times), ""
        ) # WARN: no end comma for last JSON element
        to_string += "}"

        return to_string
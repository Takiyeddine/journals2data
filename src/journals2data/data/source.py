import typing
from typing import List, Dict, TYPE_CHECKING
import json

import journals2data
from journals2data import console

# avoid circular import for type checking
#if TYPE_CHECKING:
#    from .article import Article


class Source:

    params: dict # instead of config due to circular import

    url: str
    language: str
    html: str
    scrap_frequency: str
    output_filepath: str

    # list of ongoing article urls to Article
    #articles: typing.Optional[List[Article]]
    
    def __init__(
        self, 
        url: str, 
        language: str, 
        params: dict,
        html: str = "",
        scrap_frequency: str = "",
        output_filepath: str = "",
        #articles: typing.Optional[List[Article]] = None
    ):
        self.url = url
        self.language = language
        self.html = html
        self.scrap_frequency = scrap_frequency
        self.params = params

        if(
            output_filepath == "" or
            output_filepath == "null" or
            output_filepath == "None"
        ):
            self.output_filepath = self.params["DEFAULT_OUTPUT_FILEPATH"]
        else:
            self.output_filepath = output_filepath
        
        #if(articles == None):
        #    self.articles = []
        #else:
        #    self.articles = articles
    
    def set_html(self, html: str):
        self.html = html
    
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
            "language", str(self.language)
        )
        to_string += __pretty_color_line(
            "scrap_frequency", str(self.scrap_frequency)
        )
        to_string += __pretty_color_line(
            "output_filepath", str(self.output_filepath), ""
        ) # WARN: no end comma for last JSON element
        to_string += "}"

        return to_string



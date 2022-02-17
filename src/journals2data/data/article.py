from logging import log
import typing
from typing import Dict, List
import json
import os
import datetime

import pandas

from elasticsearch import Elasticsearch
es = Elasticsearch()

from .source import Source
from journals2data import console
from journals2data import utils

class Article():

    source: Source
    raw_html: str

    # to be save
    url: str
    url_source: str
    language: str
    timestamp_start: str
    timestamp_end: str
    title_from_source: str
    title_from_page: str
    full_text: str
    publish_date: str
    timestamp_scraping: str

    # WARN: default arguments must be at the end
    def __init__(
        self,
        source: Source,
        url: str,
        title: str = "",
        full_text: str = "",
        timestamp_start: str = "",
        timestamp_end: str = "",
        title_from_source: str = "",
        timestamp_scraping: str = ""
    ):
        self.source = source
        self.url = url
        self.title = title
        self.full_text = full_text
        self.timestamp_start = timestamp_start
        self.timestamp_end = timestamp_end
        self.title_from_source = title_from_source
        self.timestamp_scraping = timestamp_scraping

        # from Source object
        self.language = source.language
        self.url_source = source.url

        self.publish_date = ""
        self.title_from_page = ""
    
    def set_full_text(self, text: str):
        self.full_text = text.replace("\n", "")  # remove \n
    
    def __str__(self) -> str:
        return self.to_str(
            pretty = False,
            colors = False
        )
    
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
            for _ in range(nb_spaces):
                spaces += " "
        print
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
            "url_source", str(self.url_source)
        )
        to_string += __pretty_color_line(
            "language", str(self.language)
        )

        to_string += __pretty_color_line(
            "title_from_source", str(self.title_from_source)
        )
        to_string += __pretty_color_line(
            "title_from_page", str(self.title_from_page)
        )
        to_string += __pretty_color_line(
            "full_text", str(self.full_text)
        )
        to_string += __pretty_color_line(
            "publish_date", str(self.publish_date)
        )
        to_string += __pretty_color_line(
            "timestamp_scraping", str(self.timestamp_scraping), ""
        )        
         # WARN: no end comma for last JSON element
        to_string += "}"

        return to_string

    def save(self):
        """
        Save the article data if it make sense to do so 
        (not empty). 
        NOTE: The saving method used for the article depends on
        the conf param ARTICLE_SAVING_OPTION.
        """
        if(
            self.full_text == "" or
            self.source.params["ARTICLE_SAVING_OPTION"] ==
            utils.ArticleSavingOption.NO_SAVING
        ):
            # VERB: log article not saved
            utils.log(
                self.source.params["VERBOSE"],
                "Article [" + self.url + "] [txt: " + \
                utils.limit_line_str(self.full_text) + "] " + \
                "not saved!",
                console.ANSIColorCode.MISSED_C
            )
        elif(
            self.source.params["ARTICLE_SAVING_OPTION"] ==
            utils.ArticleSavingOption.SAVE_TO_FILE
        ):
            self.__save_to_file()

        elif(
            self.source.params["ARTICLE_SAVING_OPTION"] ==
            utils.ArticleSavingOption.SAVE_TO_ELASTICSEARCH
        ):
            self.__save_to_elasticsearch()

    def __save_to_file(self):
        """
        This function is responsible for saving the object as
        a JSON object.

        TODO: Add verification that the object is not already
        in the file.
        TODO: While implementing threading, make sure no concurrent
        writing can occur.
        """
        filepath: str = self.source.output_filepath
        endl: str = "\n"

        # if file does not exist or is empty, create one with empty JSON list
        if(
            os.path.exists(filepath) == False or
            os.path.getsize(filepath) == 0
        ):
            with open(
                filepath, encoding = 'utf-8', mode = 'w'
            ) as file:
                file.write(
                    "[" + endl + "]"
                )

        with open(
            filepath, encoding = 'utf-8', mode = 'r+'
        ) as file:
            lines: List[str] = file.readlines()
            nb_of_lines: int = len(lines)

            # insert line at a line before the last one
            #    + StackOverflow: https://stackoverflow.com/questions/1325905/inserting-line-at-specified-position-of-a-text-file
            spaces: str = "    "
            lines.insert(nb_of_lines - 1, spaces + str(self) + endl)

            # check if preceding line needs a ',' at its end
            line_before_insertion: str = lines[nb_of_lines - 2]
            if(
                line_before_insertion[:1] != '[' and
                line_before_insertion[:1] != ']'
            ):
                lines[nb_of_lines - 2] = line_before_insertion.strip('\n') + "," + endl

            file.seek(0)
            file.writelines(lines)

        # logging
        if(self.source.params["VERBOSE"].value > 0):
            url_preview = utils.limit_line_str(self.url)
            print(
                "Article saved: [url: " + url_preview + "] " +
                "at " + filepath
            )

    def __save_to_elasticsearch(self):
        """
        This function wraps up the article into a JSON object in a proper format and indexes it into an
        Elasticsearch cluster
        """
        es = Elasticsearch([self.source.params["ES_HOST"]],
                           http_auth=(self.source.params['ES_USER'], self.source.params['ES_PASSWORD']),
                           port=self.source.params['ES_PORT'])
        doc = {
            'author': self.url_source,
            'title': self.title_from_page,
            'body': self.full_text,
            'created_at': self.publish_date,
            'title': self.title_from_page,
            'link': self.url,
            'scrapped_at': self.timestamp_scraping
        }

        index = self.source.params["ES_INDEX"]
        res = es.index(index=index, id=self.url, body=doc)
        print(res['result'])
        print("\nSaved !!!!\n")

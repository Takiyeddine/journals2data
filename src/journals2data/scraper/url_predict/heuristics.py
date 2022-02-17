import re
import pandas as pd


def apply_heuristic_h0(
    dataframe: pd.DataFrame
) -> pd.DataFrame:

    def heuristic_0(title):
        """
        Consider that any URL with a title containing less
        """
        if (len(title.split()) < 4):
            return 0 # not a good link
        else:
            return 1

    dataframe['h0'] = 0
    dataframe['h0'] = dataframe.apply(
        lambda x: heuristic_0(x.title), axis=1
    )

    return dataframe

def apply_heuristic_h1(dataframe: pd.DataFrame) -> pd.DataFrame:

    def substring(string, start, end):
        return string[start:end]

    def link_contains_blank_space_or_not_http(link: str) -> bool:
        if link.count(' ') > 0 or substring(link, 0, 4) != "http":
            return True
        else:
            return False

    def heuristic_1(link: str) -> int:
        """
        This heuristic checks a number of parameters:
        + absence of blank spaces in URL string  
        + string starts with 'http' (hence string != '')
        """
        link = str(link) # IMPORTANT : needed for interpreting type correctly (int by default)
        if link_contains_blank_space_or_not_http(link):
            return 0
        else:
            return 1
    
    dataframe['h1'] = 0 # add column for results
    dataframe['h1'] = dataframe["URL"].apply(heuristic_1)

    return dataframe

def apply_heuristic_h2(dataframe: pd.DataFrame) -> pd.DataFrame:

    def heuristic_2(link: str) -> int:
        """
        Check the presence of http(s)?://stuff/stuff
        """
        link = str(link) # IMPORTANT : needed for interpreting type correctly
        regex = re.compile("\A(http|https)://(\S*)/\w(\S*)$")
        result = re.match(regex, link)
        if isinstance(result, re.Match):
            return 1
        else:
            return 0
    
    dataframe['h2'] = 0 # add column for results
    dataframe['h2'] = dataframe["URL"].apply(heuristic_2)

    return dataframe

def apply_heuristic_h3(dataframe: pd.DataFrame) -> pd.DataFrame:

    def heuristic_3(link: str) -> int:
        """
        Checks the presence of a date in the provided string
        """
        link = str(link) # IMPORTANT : needed for interpreting type correctly
        results: list = []

        # 2021-02-16 ([1-2]***-[0-1]*-[0-3]*) ---> "[1-2]\d{3}(_|-|/|)?[0-1]\d(_|-|/)?[0-3]\d"
        # or 2021/apr/20 ---> need to match months in letters
        # (?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)
        # StackOverflow : https://stackoverflow.com/questions/2655476/regex-to-match-month-name-followed-by-year 
        regex = re.compile(
            "[1-2]\d{3}(_|-|/|)?([0-1]\d|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?))(_|-|/)?[0-3]\d",
            re.IGNORECASE # use this instead of (?i) because it's deprecated
        )
        results.append(re.search(regex, link))

        # 13-02-2021 (inverted order) 
        regex = re.compile(
            "[0-3]\d(_|-|/|)?([0-1]\d|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?))(_|-|/)?[1-2]\d{3}",
            re.IGNORECASE # use this instead of (?i) because it's deprecated
        )
        results.append(re.search(regex, link))

        # check for results
        for result in results:
            if isinstance(result, re.Match):
                return 1
        
        # in case no results was found
        return 0
    
    dataframe['h3'] = 0 # add column for results
    dataframe['h3'] = dataframe['URL'].apply(heuristic_3)

    return dataframe


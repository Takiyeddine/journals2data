# manual testing of journals2data objects

# run at ".." level
from context import get_python_run_context
get_python_run_context()

import json
import datetime as dt

# personal imports
from journals2data import utils
from journals2data import console
from journals2data import data



# check data.Source conversion to str
test_source: data.Source = data.Source('a', 'b', "c")
console.println_debug("****** data.Source.__str__() ")
print(str(test_source))
console.println_debug("******* data.Source.to_str() ")
print(test_source.to_str())

# check data.Source conversion to dict
console.println_debug("****** Source to Dict")
source_json: str = str(test_source)
source_dict: dict = json.loads(source_json)
utils.print_pretty_json(source_dict)
# test casting
console.println_debug("****** Source to Dict casting")
source_dict_casted: dict = test_source.to_dict()
utils.print_pretty_json(source_dict_casted)



# check data.Article conversion to str
console.println_debug("****** data.Article.__str__() ")
test_article: data.Article = data.Article(
    test_source,
    "https://www.test.com/test.html",
    "Test",
    "This is just a simple test.",
    dt.datetime.now().strftime("%S_%M_%H_%d_%m_%Y"),
    None,
    None
)
print(str(test_article))
console.println_debug("******* data.Article.to_str() ")
print(test_article.to_str())

# check data.Article conversion to dict
console.println_debug("****** data.Article to Dict")
article_json: str = str(test_article)
article_dict: dict = json.loads(article_json)
utils.print_pretty_json(article_dict)
# test casting
console.println_debug("****** data.Article to Dict casting")
article_dict_casted: dict = test_article.to_dict()
utils.print_pretty_json(article_dict_casted)



# check Article writing to a file
test_article.save_to_file()


# check Article creation and scraping from real URL
scrap_test_source: data.Source = data.Source(
    "https://eu.usatoday.com/",
    "en",
    "20"
)
scrap_test_article: data.Article = data.Article(
    scrap_test_source,
    "https://eu.usatoday.com/story/news/world/2021/06/14/vladimir-putin-refuses-guarantee-alexei-navalnys-safety-prison/7682827002/",
)
console.println_debug("****** data.Article before scraping")
print(scrap_test_article.to_str())
scrap_test_article.scrap()
console.println_debug("****** data.Article after scraping")
print(scrap_test_article.to_str())

# TODO: install latest version of Python, because of strong typing pb

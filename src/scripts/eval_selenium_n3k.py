# this script is based on scraped html from scrap_raw_article_html.py
# using selenium
#    + run: python3 src/scripts/eval_selenium_n3k.py  (from journals2data top dir, not src)

# measure execution time
#    + https://datatofish.com/measure-time-to-run-python-script/ 
import time
start_time = time.time()

# run at ".." level
from context import get_python_run_context
get_python_run_context()

# debug module imports
import os
DEBUG: bool = True
if DEBUG:
    print(
        "Python Current Working directory = " + str(os.getcwd())
    )

import nltk

from journals2data import data
from journals2data import console
from journals2data import utils

# script flags
VERBOSE: bool = False

# data inputs
urls = utils.json_file_to_data(
    "./res/raw_html_articles/articles_clean.json"
)

# data outputs
results_outfile_path = "./out/scripts/test_selenium_n3k_3.json"
results = {
    "execution_time": "null",
    "avg_relative_diff": "null",
    "article_results_list": []
}


relative_diffs = []

for element in urls:
    # scrap with n3k
    source = data.Source(
        "",
        "en"
    )
    article = data.Article(
        source,
        element["url"]
    )
    # passing raw html from selenium to parse
    article.scrap(element["html"])

    # anounce new element
    console.println_ctrl_sequence(
        "****** ****** ****** element[\"url\"] = " + element["url"],
        console.ANSICtrlSequence.PASSED
    )

    # compute score
    if(VERBOSE):
        console.println_debug("****** scraping phase")
    n3k = article.full_text
    if(n3k == None):
        n3k = "error, nothing scraped"
    if(VERBOSE):
        console.println_debug("*** n3k")
        print("\"n3k\": " + n3k)

    # FIXED: Article.download() takes optional param for raw html
    manual = element["manual"]
    if(VERBOSE):
        console.println_debug("*** manual")
        print("\"manual\": " + manual)

    #distance calculation
    distance=nltk.edit_distance(n3k , manual)
    maxlen = max(len(n3k), len(manual))

    relative_diff = (float(maxlen - distance)/float(maxlen))*100
    relative_diffs.append(relative_diff)

    console.println_debug("****** relative_diff")
    print("score = " + str(relative_diff) + "%")

    # add to results
    article_results = {}
    article_results["url"] = element["url"]
    article_results["n3k"] = n3k
    article_results["manual"] = manual
    article_results["maxlen"] = maxlen
    article_results["distance"] = distance
    article_results["score"] = relative_diff

    results["article_results_list"].append(article_results)


# general info
console.println_ctrl_sequence(
    "****** ****** ****** general info",
    console.ANSICtrlSequence.PASSED
)

# compute avg relative difference
avg_relative_diff: float = 0
for diff in relative_diffs:
    avg_relative_diff += diff
avg_relative_diff = (
    avg_relative_diff/float(len(relative_diffs))
)
print(
    "Average relative difference: " + 
    str(avg_relative_diff)
)

# get script execution time
execution_time = (time.time() - start_time)
print('Execution time in seconds: ' + str(execution_time))



# add to results
results["avg_relative_diff"] = avg_relative_diff
results["execution_time"] = execution_time

# save results to file
utils.save_json_to_file(results, results_outfile_path)

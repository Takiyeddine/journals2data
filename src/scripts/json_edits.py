import os
print(
    "Python Current Working directory = " + str(os.getcwd())
)

# run at ".." level
from context import get_python_run_context
get_python_run_context()

from journals2data import data
from journals2data import console
from journals2data import utils

results = utils.json_file_to_data(
    "./out/scripts/test_selenium_n3k.json"
)

for element in results["article_results_list"]:
    console.println_debug("**************")
    print(element["n3k"])
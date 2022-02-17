# this script test journals2data api!

# measure execution time
#    + https://datatofish.com/measure-time-to-run-python-script/ 
import time
start_time = time.time()

# run at ".." level
from context import get_python_run_context
get_python_run_context()

import journals2data
from journals2data import data
from journals2data import console
from journals2data import utils

# debug module imports
import os
print(
    "Python Current Working directory = " + str(os.getcwd())
)

# get script params
import argparse
parser = argparse.ArgumentParser(description='TryJ2D')
parser.add_argument(
    '--conf_path', 
    type=str, 
    default="/home/onyr/Documents/code/python/journals2data/src/journals2data/conf/journals2data.onyr.conf",
    help='url used to retrieve the articles'
)
args = parser.parse_args()



# run journals2data library
import sys
if (args.conf_path):
    console.println_debug(
        "****** running J2D [--conf_path: " +
        args.conf_path + "]"
    )

    config = journals2data.J2DConfiguration(
        args.conf_path
    )
    collector = journals2data.Journals2Data(
        config
    )
    collector.scrap()
else:
    sys.exit(
        """
        Error: No argument given to script. 
        Please provide a --conf_path
        param to the script, giving the path of the conf file
        to execute the library on.
        """
    )


# get script execution time
execution_time = (time.time() - start_time)
print('Execution time in seconds: ' + str(execution_time))
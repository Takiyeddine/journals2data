# This file manages the library and provides to the user a CLI
# to interact with the library directly.
# It calls the journals2data object-oriented api

# tuto: https://realpython.com/command-line-interfaces-python-argparse/
# doc: https://docs.python.org/3/library/argparse.html 

# measure total execution time
#    + https://datatofish.com/measure-time-to-run-python-script/ 
from argparse import Namespace
import time
start_time = time.time()

# run at .. level
import os
import sys
cur_dir = os.path.dirname(os.path.realpath(__file__))
top_dir = os.path.abspath(os.path.join(cur_dir, os.pardir))
sys.path.append(top_dir)
print(
    "Python Current Working directory = " + str(os.getcwd())
)

# 2FIX: circular import: $ python3 src/journals2data/cli.py
#  ImportError: attempted relative import with no known parent package
# executing a module
from .configuration import J2DConfiguration
from .journals2data import Journals2Data

def main(conf_path: str):

    # run journals2data library
    import sys
    if(conf_path):
        print(
            "****** running J2D [--conf_path: " +
            conf_path + "]"
        )
        new_config = J2DConfiguration(
            conf_path
        )
        j2d = Journals2Data(
            config=new_config
        )
        j2d.master_scraper.scheduled_sync_scrap()
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

if __name__ == '__main__':

    # get script params
    import argparse
    parser = argparse.ArgumentParser(description='TryJ2D')
    parser.add_argument(
        '--conf_path', 
        type=str, 
        default="D:\PFE\Dev\Journal2data\src\journals2data\conf\journals2data.onyr.conf",
        help='url used to retrieve the articles'
    )
    args = parser.parse_args()

    # run script
    main(args.conf_path)
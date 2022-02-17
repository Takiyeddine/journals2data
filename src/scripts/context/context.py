import os
import sys

def get_python_run_context():
    # Add ".." to module search path
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    top_dir = os.path.abspath(os.path.join(cur_dir, os.pardir))
    top_dir2 = os.path.abspath(os.path.join(top_dir, os.pardir))
    sys.path.append(top_dir2)

# manual testing for the sub-module console

# run at ".." level
from context import get_python_run_context
get_python_run_context()

from journals2data import console

console.println_debug("hello world")
console.println_ctrl_sequence(
    "hello world :)",
    console.ANSICtrlSequence.FAILED
)
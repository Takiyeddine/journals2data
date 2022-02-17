from typing import Any

import signal
from journals2data import exception

# StackOverflow: https://stackoverflow.com/questions/2196999/how-to-add-a-timeout-to-a-function-in-python/2197148#2197148 
# decorators: https://ron.sh/how-to-write-custom-python-decorators/ 
# signal for timeout: https://code-maven.com/python-timeout 

def syncTimeout(limit: int):
    """
    Decorator for adding timeout to a synchronous function.

    WARN: Thows exception.Timeout() if timeout limit is reached.

    TODO: for now, only available on UNIX due to the use of 
    the signal module.
    See doc: https://docs.python.org/2.7/library/signal.html#signal.alarm 
    See StackOverflow: https://stackoverflow.com/questions/35490555/python-timeout-decorator 
    See better GitHub: https://github.com/bitranox/wrapt_timeout_decorator 
    """
    # check parameter
    if limit <= 0:
        raise ValueError(
            "Please, provide a positive timeout value."
        )
    
    # signal handler
    def __alarm_handler(signum, frame):
        raise exception.Timeout("ALARM signal received")

    # wrap decorated function
    def wrap(function):
        def __sync_timeout(*args, **kwargs):
            # set up ALRM signal from OS
            signal.signal(signal.SIGALRM, __alarm_handler)
            signal.alarm(limit)

            # run function
            result = None
            try:
                result = function(*args, **kwargs)
            finally:
                signal.alarm(0) # turn ALRM signal off

            return result
        return __sync_timeout
    return wrap


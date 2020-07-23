import time


def stopwatch(function, positional_args):
    start = time.time()
    function(*positional_args)
    end = time.time()
    duration = end - start
    return duration

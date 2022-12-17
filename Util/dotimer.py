import signal


class TimeoutExpired(Exception):
    pass


def alarm_handler(signum, frame):
    raise TimeoutExpired


def do_intime(time_function,end_time_function,timeout):
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout) 

    try:
        return time_function()
    except TimeoutExpired:
        signal.alarm(0) 
        end_time_function()
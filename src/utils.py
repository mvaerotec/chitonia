from datetime import datetime
from enum import IntEnum

class Points(IntEnum):
    INITIAL_VAL = 15
    DECREASE = 2
    SMALL_INC = 2
    MED_INC = 5
    BIG_INC = 7


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

#from datetime import datetime, timedelta

#def add(moment):
#   return(moment + timedelta(seconds = 1e9))


import datetime
def add (moment):
    time_change = datetime.timedelta(seconds=1e9)
    new_time = moment + time_change
    return new_time

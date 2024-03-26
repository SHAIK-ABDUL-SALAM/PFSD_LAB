import datetime
import time
import calendar
print(time.time())
print(time.asctime())

var=datetime.datetime.now()
print("year",var.year)

s=calendar.prcal(2023)
s1=calendar.month(2023,4)
s2=calendar.isleap(2023)
print(s)

x=datetime.datetime.now()
from datetime import timedelta
print(x+timedelta(days=-1))

import pytz
from datetime import datetime
time1=pytz.timezone('Europe/Berlin')
time2=pytz.timezone('America/Havana')
print(datetime.now(time2))

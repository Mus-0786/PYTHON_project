#!/usr/bin/python
import time
import datetime
from lib import tm1637 as obj
Display = obj.TM1637(15, 14, 5)
Display.Clear()
while(True):
 now = datetime.datetime.now()
 hour = now.hour
 minute = now.minute
 second = now.second
 Display.Clear()
 val = [(int(hour / 10)), (hour % 10), (int(minute / 10)), (minute % 10) ]
 Display.Show(val)
 Display.ShowDoublepoint((second % 2))
 time.sleep(0

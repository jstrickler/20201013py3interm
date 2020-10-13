#!/usr/bin/env python
from datetime import date, time, datetime
import time as Time

my_time = time(10, 42, 51)   # <1>
my_date = date(1996, 1, 31)  # <2>
my_datetime = datetime(1996, 1, 31, 10, 42, 51)  # <3>
my_timestamp = my_datetime.timestamp()  # <4>
my_timetuple = my_datetime.timetuple()  # <5>

print("my_time:", my_time)
print("my_date:", my_date)
print("my_datetime:", my_datetime)
print("my_timestamp:", my_timestamp)
print("my_timetuple:", my_timetuple)
print()

d = my_datetime.date() # <6>
print("datetime -> date:", d)

t = my_datetime.time() # <7>
print("datetime -> time:", t)

ts = my_datetime.timestamp() # <8>
print("datetime -> timestamp:", ts)

tt = my_datetime.timetuple() # <9>
print("datetime -> timetuple:", tt)
print()

dt = datetime.fromordinal(my_date.toordinal())  # <10>
print("date -> datetime:", dt)

t = datetime.fromordinal(my_date.toordinal()).time() # <11>
print("date -> time:", t)

ts = datetime.fromordinal(my_date.toordinal()).timestamp()  # <12>
print("date -> timestamp:", ts)

tt = my_date.timetuple() # <13>
print("date -> timetuple:", tt)
print()

dt = my_datetime.fromtimestamp(my_timestamp)  # <14>
print("timestamp -> datetime:", dt)

d = my_datetime.fromtimestamp(my_timestamp).date()  # <15>
print("timestamp -> date:", d)

t = my_datetime.fromtimestamp(my_timestamp).time()  # <16>
print("timestamp -> datetime:", t)

tt = Time.localtime(my_timestamp)
print("timestamp -> timetuple:", tt)  # <17>
print()

dt = datetime.fromtimestamp(Time.mktime(my_timetuple))  # <18>
print("timetuple -> datetime:", dt)

d = datetime.fromtimestamp(Time.mktime(my_timetuple)).date() # <19>
print("timetuple -> date:", d)

dt = datetime.fromtimestamp(Time.mktime(my_timetuple))  # <20>
print("timetuple -> time:", t)

ts = Time.mktime(my_timetuple)  # <21>
print("timetuple -> timestamp:", ts)

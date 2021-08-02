from datetime import datetime
from datetime import timedelta

time = datetime(2020, 11, 4, 14, 53)
print(time.strftime("%Y/%m/%d %H:%M:%S"))
print(time.strftime("%y/%B/%d %H:%M:%S %p"))
print(time.strftime("%a, %Y %b %d"))
print(time.strftime("%A, %Y %B %d"))
print("Weekday:", time.strftime("%w"))
print("Day of the year:", time.strftime("%j"))
print("Week number of the year:", time.strftime("%U"))

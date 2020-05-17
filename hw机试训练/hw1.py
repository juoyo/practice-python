#coding=utf-8
# 1980 01 02 5|1980 01 04
import datetime
s = input()
d1, d2 = s.split("|")
year1, month1, day1, tempxq = d1.split()
year2, month2, day2 = d2.split()
date1 = datetime.date(year=int(year1), month=int(month1), day=int(day1))
date2 = datetime.date(year=int(year2), month=int(month2), day=int(day2))
day = (date2 - date1).days
allday = int(tempxq) + day
while allday > 7:
    allday = allday - 7
print(allday)

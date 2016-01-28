import datetime
from collections import Counter

dayOfWeek = [datetime.date(year,month,1).weekday() for year in range(1901,2001) for month in range(1,13)]

c = Counter(dayOfWeek)

print "Using datetime library"
print c[6] 


monthLengths = [31,28,31,30,31,30,31,31,30,31,30,31]

sundays = 0
dayOfWeek = 1 # Jan 1 1901 was a Tuesday

for year in range(1901,2001):
	for month in range(12):
		if dayOfWeek == 6:
			sundays += 1 

		dayOfWeek = (dayOfWeek+monthLengths[month])%7
		if month == 1 and  ((year%4==0 and not year%100==0) or year%400==0):
			dayOfWeek=(dayOfWeek+1)%7


print "Without datetime"
print sundays


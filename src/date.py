import datetime
from datetime import date
print 'date.fromordinal(730920)'
d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
print d
print datetime.date(2002, 3, 11)

print
print 'timetuple'
t = d.timetuple()
for i in t:     
	print i

print
print 'isocalendar'
ic = d.isocalendar()
for i in ic:    
	print i

print
print 'isoformat'
print d.isoformat()

print
print 'strftime'
print d.strftime("%d/%m/%y")

print
print  d.strftime("%A %d. %B %Y")
print 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")

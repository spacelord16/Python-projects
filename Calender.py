import calendar

y = int(input("Enter Year"))
m = int(input("Enter month"))
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(y, m)
print(str)

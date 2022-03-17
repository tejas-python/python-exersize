# print data time
import datetime
time = datetime.datetime.now()
print(time.strftime("Today is %A, %B %d, %Y"))
'''%A day of the week in words
%B month name full name
%d day of the month
%Y year '''


'''
We're using datetime  standard module here, which supplies classes to manipulate dates and times. Note that datetime.now()  would produce 2016-12-25 22:54:34.153209, which is a datetime  object. However, by applying strftime (string from time), we convert that object to a readable string using format codes. For example, %A  would extract the day, %B  the month, %d  the date, and %Y  the year. You can find the complete list of format codes on the strftime.org website.'''

days = int(input('number of days: '))
hours = int(input('number of hours: '))
minutes = int(input('number of minutes: '))
seconds = int(input('number of seconds: '))

sec_result = ((days*24 + hours)*60 + minutes)*60 + seconds
print('The given time equals', sec_result, 'seconds')

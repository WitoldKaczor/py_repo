day = int(input('Input the day: '))
month = input('Input the month: ')
month = month.lower()

if day == 1 and (month == 'january' or month == 'jan'):
    print('New year’s day')
elif day == 1 and month == 'july':
    print('Canada day')
elif day == 25 and (month == 'december' or month == 'dec'):
    print('Christmas day')
else:
    print('No fixed-date holiday in Canada')

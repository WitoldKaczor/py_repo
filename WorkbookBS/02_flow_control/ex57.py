while True:
    year = int(input('Input a year: '))

    if year % 400 == 0:
        leap_year = True
    elif year % 400 != 0 and year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False

    if leap_year:
        print('%d is a leap year' % year)
    else:
        print('%d is not a leap year' % year)

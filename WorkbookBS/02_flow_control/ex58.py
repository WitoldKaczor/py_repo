while True:
    print('Enter a date in format DD-MM-YYYY')
    date = input()

    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])

    if day < 1 or day > 31:
        print('Invalid input')
    elif month < 1 or month > 12:
        print('Invalid input')
    elif year < 0:
        print('Invalid input')
    else:
        dayNew = day
        monthNew = month
        yearNew = year

        if year % 400 == 0:
            leap_year = True
        elif year % 400 != 0 and year % 100 == 0:
            leap_year = False
        elif year % 4 == 0:
            leap_year = True
        else:
            leap_year = False

        if (month in [1, 3, 5, 7, 8, 10, 12] and day < 31) \
                or (month in [4, 6, 9, 11] and day < 30):
            dayNew += 1
        elif month == 2 and ((leap_year and day < 29) or (not leap_year and day < 28)):
            dayNew += 1
        elif month != 12:
            dayNew = 1
            monthNew += 1
        elif month == 12:
            dayNew = 1
            monthNew = 1
            yearNew += 1

        print('The day immediately after %02d-%02d-%04d is %02d-%02d-%04d'
              % (day, month, year, dayNew, monthNew, yearNew))

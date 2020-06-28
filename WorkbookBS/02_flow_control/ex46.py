# Spring March 20
# Summer June 21
# Fall September 22
# Winter December 21

while True:
    day = int(input('day: '))
    month = input('month: ')
    month = month.lower()

    months = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']

    if day < 1 or day > 31 or month not in months:
        print('Invalid input')
    elif (month == 'april' or month == 'june' or month == 'september' or month == 'november') and day == 31:
        print('Invalid input')
    elif month == 'february' and day > 29:
        print('Invalid input')
    else:
        if (month == 'march' and day >= 20) or month == 'april' or \
                month == 'may' or (month == 'june' and day < 21):
            season = 'spring'
        elif (month == 'june' and day >= 21) or month == 'july' or \
                month == 'august' or (month == 'september' and day < 22):
            season = 'summer'
        elif (month == 'september' and day >= 22) or month == 'october' or \
                month == 'november' or (month == 'december' and day < 21):
            season = 'autumn'
        else:
            season = 'winter'
        print("it's", season)

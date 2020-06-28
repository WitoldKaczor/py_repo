while True:
    print(5*'-', 'Enter your birthday', 5*'-')
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
        if (month == 'december' and day >= 22) or (month == 'january' and day <= 19):
            zodiac_sign = 'Capricorn'
        elif (month == 'january' and day >= 20) or (month == 'february' and day <= 18):
            zodiac_sign = 'Aquarius'
        elif (month == 'february' and day >= 19) or (month == 'march' and day <= 20):
            zodiac_sign = 'Pisces'
        elif (month == 'march' and day >= 21) or (month == 'april' and day <= 19):
            zodiac_sign = 'Aries'
        elif (month == 'april' and day >= 20) or (month == 'may' and day <= 20):
            zodiac_sign = 'Taurus'
        elif (month == 'may' and day >= 21) or (month == 'june' and day <= 20):
            zodiac_sign = 'Gemini'
        elif (month == 'june' and day >= 21) or (month == 'july' and day <= 22):
            zodiac_sign = 'Cancer'
        elif (month == 'july' and day >= 23) or (month == 'august' and day <= 22):
            zodiac_sign = 'Leo'
        elif (month == 'august' and day >= 23) or (month == 'september' and day <= 22):
            zodiac_sign = 'Virgo'
        elif (month == 'september' and day >= 23) or (month == 'october' and day <= 22):
            zodiac_sign = 'Libra'
        elif (month == 'october' and day >= 23) or (month == 'november' and day <= 21):
            zodiac_sign = 'Scorpio'
        else:
            zodiac_sign = 'Sagittarius'

        print('Your zodiac sign is', zodiac_sign)
    print()

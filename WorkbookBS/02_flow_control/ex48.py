# 2000 Dragon
# 2001 Snake
# 2002 Horse
# 2003 Sheep
# 2004 Monkey
# 2005 Rooster
# 2006 Dog
# 2007 Pig
# 2008 Rat
# 2009 Ox
# 2010 Tiger
# 2011 Hare

while True:
    year = int(input('Enter a year: '))

    if year < 0:
        print('Invalid year')
    else:
        x = (year - 2000) % 12

        if x == 0:
            chin_zod_sign = 'Dragon'
        elif x == 1:
            chin_zod_sign = 'Snake'
        elif x == 2:
            chin_zod_sign = 'Horse'
        elif x == 3:
            chin_zod_sign = 'Sheep'
        elif x == 4:
            chin_zod_sign = 'Monkey'
        elif x == 5:
            chin_zod_sign = 'Rooster'
        elif x == 6:
            chin_zod_sign = 'Dog'
        elif x == 7:
            chin_zod_sign = 'Pig'
        elif x == 8:
            chin_zod_sign = 'Rat'
        elif x == 9:
            chin_zod_sign = 'Ox'
        elif x == 10:
            chin_zod_sign = 'Tiger'
        elif x == 11:
            chin_zod_sign = 'Hare'

        print('The year %d is year of %s' % (year, chin_zod_sign))

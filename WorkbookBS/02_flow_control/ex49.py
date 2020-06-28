# Less than 2.0 Micro
# 2.0 to less than 3.0 Very minor
# 3.0 to less than 4.0 Minor
# 4.0 to less than 5.0 Light
# 5.0 to less than 6.0 Moderate
# 6.0 to less than 7.0 Strong
# 7.0 to less than 8.0 Major
# 8.0 to less than 10.0 Great
# 10.0 or more Meteoric
while True:
    magnitude = float(input('Input earthquake magnitude: '))

    if magnitude < 0.0:
        print('Magnitude cannot be negative')
    else:
        if magnitude < 2.0:
            descriptor = 'micro'
        elif 2.0 <= magnitude < 3.0:
            descriptor = 'very minor'
        elif 3.0 <= magnitude < 4.0:
            descriptor = 'minor'
        elif 4.0 <= magnitude < 5.0:
            descriptor = 'light'
        elif 5.0 <= magnitude < 6.0:
            descriptor = 'moderate'
        elif 6.0 <= magnitude < 7.0:
            descriptor = 'strong'
        elif 7.0 <= magnitude < 8.0:
            descriptor = 'major'
        elif 8.0 <= magnitude < 10.0:
            descriptor = 'great'
        elif 10.0 < magnitude:
            descriptor = 'meteoric'

        print('magnitude %.1f earthquake is considered to be a %s earthquake' % (magnitude, descriptor))

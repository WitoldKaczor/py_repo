print('Height')
height_feet = float(input('feet: '))
height_inch = float(input('inches: '))

height_cm = (height_feet*12 + height_inch) * 2.54
print('Height in cm: {:.2f}'.format(height_cm))

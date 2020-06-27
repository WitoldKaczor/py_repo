from math import pi

radius = float(input('Input radius of cylinder: '))
height = float(input('Input height of cylinder: '))

volume = pi * radius**2 * height

print('Volume of the cylinder equals {:.1f}'.format(volume))

from math import pi

radius = float(input('Input radius: '))

area = pi * radius**2
volume = 4/3 * pi * radius**3

print('Area of a circle with radius {:.2f} equals {:.2f}'.format(radius, area))
print('Volume of a sphere with radius {:.2f} equals {:.2f}'.format(radius, volume))

from math import tan, pi

print(5*'-', 'Area of regular polygon', 5*'-')
s = float(input('length of a polygon side: '))
n = float(input('number of polygon sides: '))

area = (n * s**2) / (4 * tan(pi/n))
print('Area of the polygon equals {:.2f}'.format(area))

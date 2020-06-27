from math import sqrt

s1 = float(input('first side of triangle: '))
s2 = float(input('second side of triangle: '))
s3 = float(input('third side of triangle: '))

s = (s1 + s2 + s3) / 2

area = sqrt(s * (s-s1) * (s-s2) * (s-s3))
print('area of triangle equals {:.2f}'.format(area))

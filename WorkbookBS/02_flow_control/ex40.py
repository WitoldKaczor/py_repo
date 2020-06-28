side1 = int(input('length of first side: '))
side2 = int(input('length of second side: '))
side3 = int(input('length of third side: '))

if side1 == side2 and side2 == side3:
    print('This triangle is an equilateral triangle')
elif side1 != side2 and side2 != side3 and side3 != side1:
    print('This triangle is an scalene triangle')
else:
    print('This triangle is an isosceles triangle')

def hypotenuse(side_a, side_b):
    if side_a < 0 or side_b < 0:
        print('only non-negative numbers allowed')
        return 0
    else:
        from math import sqrt
        return sqrt(side_a**2 + side_b**2)


a = float(input('side A: '))
b = float(input('side B: '))
print('Hypotenuse:', hypotenuse(a, b))

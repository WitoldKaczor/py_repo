from math import sqrt

print(5*'=', 'Quadratic Equation', 5*'=')
print('Input Coefficients')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if b**2 - 4*a*c < 0.0:
    print('No real roots')
elif b**2 - 4*a*c == 0.0:
    double_root = -b / (2*a)
    print('One double root %.2f' % double_root)
else:
    root1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    root2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    print('Two real roots %.2f and %.2f' % (root1, root2))

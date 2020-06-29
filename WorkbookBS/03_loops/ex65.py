from math import sqrt

print(5*'=', 'Perimeter of a Polygon', 5*'=')

ctr = 0
perimeter = 0.0
x_last = 0.0
y_last = 0.0

while True:
    print('coordinates of point P%d' % (ctr+1), '(blank to quit)')
    x = input('x{:d} = '.format(ctr+1))
    if x == '':
        break
    y = input('y{:d} = '.format(ctr+1))
    if y == '':
        break

    x = float(x)
    y = float(y)

    if ctr != 0:
        perimeter = sqrt((x_last - x)**2 + (y_last - y)**2)

    x_last = x
    y_last = y

    ctr += 1

print()
if ctr < 3:
    print('No polygon!')
else:
    print('Perimeter = %.2f' % perimeter)

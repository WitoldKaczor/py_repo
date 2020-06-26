from math import log10

a = int(input('First number: '))
b = int(input('Second number: '))

print(a, '+', b, '=', a+b)  # sum of a and b
print(a, '-', b, '=', a-b)  # difference when b is subtracted from a
print(a, '*', b, '=', a*b)  # product of a and b
print(a, '/', b, '=', a/b)  # quotient when a is divided by b
print('remainder of ', a, '/', b, ' is ', a % b, sep='')  # remainder when a is divided by b
print('log(', a, ') = {:.3f}'.format(log10(a)), sep='')  # result of log10(a)
print(a, 'to the power of', b, 'is', a**b)  # result of a**b

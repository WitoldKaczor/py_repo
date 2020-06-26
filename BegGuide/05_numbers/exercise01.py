from decimal import *

x = 3 + 4j
print(x**3.4)
print(type(x))
print(x.conjugate())
print(x.__abs__())
x += 5j
print(x)

print(bool(0))
print(bool(1))
print(bool(-3))

i = 3 * 0.1
print(i)
print(Decimal(0.1) * Decimal(3))

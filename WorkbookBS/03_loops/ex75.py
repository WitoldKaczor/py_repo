n = int(input('Input an integer: '))
m = int(input('Input an another integer: '))

d = min(abs(m), abs(n))

while abs(m) % d != 0 or abs(n) % d != 0:
    d -= 1

print('Greatest common divisor of', m, 'and', n, 'is', d)

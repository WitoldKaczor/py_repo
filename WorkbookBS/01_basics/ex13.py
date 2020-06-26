change_cents = int(input('Change in cents: '))

# init of counters
toonies = 0     # 200cents
loonies = 0     # 100cents
quarters = 0    # 25cents
dimes = 0       # 10cents
nickels = 0     # 5cents
pennies = 0     # 1cent

# loops for calculating coin numbers
while change_cents >= 200:
    change_cents -= 200
    toonies += 1
while change_cents >= 100:
    change_cents -= 100
    loonies += 1
while change_cents >= 25:
    change_cents -= 25
    quarters += 1
while change_cents >= 10:
    change_cents -= 10
    dimes += 1
while change_cents >= 5:
    change_cents -= 5
    nickels += 1
while change_cents >= 1:
    change_cents -= 1
    pennies += 1

# print change
print('The change:')

if toonies == 1:
    print(toonies, 'toonie', end='')
elif toonies > 1:
    print(toonies, 'toonies', end='')

if loonies == 1:
    print(',', loonies, 'loonie', end='')
elif loonies > 1:
    print(',', loonies, 'loonies', end='')

if quarters == 1:
    print(',', quarters, 'quarter', end='')
elif quarters > 1:
    print(',', quarters, 'quarters', end='')

if dimes == 1:
    print(',', dimes, 'dime', end='')
elif dimes > 1:
    print(',', dimes, 'dimes', end='')

if nickels == 1:
    print(',', nickels, 'nickel', end='')
elif nickels > 1:
    print(',', nickels, 'nickels', end='')

if pennies == 1:
    print(',', pennies, 'penny', end='')
elif pennies > 1:
    print(',', pennies, 'pennies')

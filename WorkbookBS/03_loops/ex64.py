print('Enter the prices in $')
print('To stop and sum up input blank line')

sm = 0.0
while True:
    price = input()
    if price == '':
        break
    sm += float(price)

sm_round = sm // (0.05-1e-6) / 20

if (sm*100) % 5 >= 2.5:
    sm_round += 0.05

print('Total:\t%.2f$' % sm)
print('Rounded:\t%.2f$' % sm_round)

INTEREST = 0.04
money = float(input('Actual savings in $: '))
years = int(input('Years of saving: '))

for i in range(1, years+1):
    money *= 1 + INTEREST
    if i == 1:
        print('Money after', i, 'year:\t\t{:.2f}'.format(money), '$')
    else:
        print('Money after', i, 'years:\t{:.2f}'.format(money), '$')

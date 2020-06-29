from random import randint

SIM_NUM = 15
CONS_FLIPS_NUM = 3

sm = 0
for i in range(0, SIM_NUM):
    ctr = 0
    ctrH = 0
    ctrT = 0
    while ctrH != CONS_FLIPS_NUM and ctrT != CONS_FLIPS_NUM:
        coin = randint(0, 1)
        if coin == 0:
            print('H  ', end='')
            ctrH += 1
            ctrT = 0
        else:
            print('T  ', end='')
            ctrT += 1
            ctrH = 0
        ctr += 1
    print('(', ctr, ' flips)', sep='')
    sm += ctr

print()
print('On average, {:.1f}'.format(sm / SIM_NUM), 'was needed')

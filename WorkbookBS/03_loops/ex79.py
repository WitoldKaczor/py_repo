from random import randint

LIMIT = 100

num = randint(1, LIMIT)
print(num, ' # init')
max_num = num
ctr = 0
for i in range(0, LIMIT-1):
    num = randint(1, LIMIT)
    if max_num < num:
        max_num = num
        print(num, ' # update')
        ctr += 1
    else:
        print(num)

print('Max value found:', max_num)
print('Number of updates:', ctr)

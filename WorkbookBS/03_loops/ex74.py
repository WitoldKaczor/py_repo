RANGE = 11

for i in range(0, RANGE):
    for j in range(0, RANGE):
        if i == 0:
            if j == 0:
                print('\t', end='')
            elif j == RANGE-1:
                print(j)
            else:
                print(j, '\t', end='')

        if j == 0 and i != 0:
            print(i, '\t', end='')

        if j != 0 and i != 0:
            if j == RANGE-1:
                print(i * j)
            else:
                print(i * j, '\t', end='')

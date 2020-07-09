def roll_dice_pair():
    from random import randint
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1+dice2


def main():
    percentage_expected = {2: 1/36*100,
                           3: 2/36*100,
                           4: 3/36*100,
                           5: 4/36*100,
                           6: 5/36*100,
                           7: 6/36*100,
                           8: 5/36*100,
                           9: 4/36*100,
                           10: 3/36*100,
                           11: 2/36*100,
                           12: 1/36*100}

    percentage_simulated = {2: 0,
                            3: 0,
                            4: 0,
                            5: 0,
                            6: 0,
                            7: 0,
                            8: 0,
                            9: 0,
                            10: 0,
                            11: 0,
                            12: 0}

    sim_num = int(1e5)
    for i in range(0, sim_num):
        result = roll_dice_pair()
        percentage_simulated[result] += 100/sim_num

    print()
    print('{:>10}'.format('Total'), '{:>10}'.format('Simulated'), '{:>10}'.format('Expected'), sep='')
    print('{:>10}'.format(' '), '{:>10}'.format('percent'), '{:>10}'.format('percent'), sep='')

    for key in percentage_expected:
        print('{:>10}'.format(key),
              '{:>10.2f}'.format(percentage_simulated[key]),
              '{:>10.2f}'.format(percentage_expected[key]), sep='')


main()

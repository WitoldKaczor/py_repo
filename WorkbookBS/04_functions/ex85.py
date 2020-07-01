def ordinal_numbers(num):
    if num == 1:
        return 'first'
    elif num == 2:
        return 'second'
    elif num == 3:
        return 'third'
    elif num == 4:
        return 'fourth'
    elif num == 5:
        return 'fifth'
    elif num == 6:
        return 'sixth'
    elif num == 7:
        return 'seventh'
    elif num == 8:
        return 'eighth'
    elif num == 9:
        return 'ninth'
    elif num == 10:
        return 'tenth'
    elif num == 11:
        return 'eleventh'
    elif num == 12:
        return 'twelfth'
    else:
        return 'n/a'


def main():
    for number in range(0, 13):
        print('Number: %d\t' % number, 'Ord.num.:', ordinal_numbers(number))

    print('Number: %d\t' % 20, 'Ord.num.:', ordinal_numbers(20))


if __name__ == '__main__':
    main()

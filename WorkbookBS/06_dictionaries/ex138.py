def create_bingo_card():
    from random import sample
    bingo_card = {'B': sample(range(1, 16), 5),
                  'I': sample(range(16, 31), 5),
                  'N': sample(range(31, 46), 5),
                  'G': sample(range(46, 61), 5),
                  'O': sample(range(61, 76), 5)}

    return bingo_card


def print_bingo_card(bingo_card):
    print()
    padding = '{:^8}'
    for char in 'BINGO':
        print(padding.format(char), end='')

    for i in range(0, 5):
        print()
        for char in 'BINGO':
            print(padding.format(bingo_card[char][i]), end='')
    print()
    return


def main():
    print_bingo_card(create_bingo_card())


if __name__ == '__main__':
    main()

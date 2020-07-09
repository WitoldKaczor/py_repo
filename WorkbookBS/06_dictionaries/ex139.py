import ex138


def check_bingo_card_if_won(bingo_card):
    # vertical check
    for char in 'BINGO':
        if sum(bingo_card[char]) == 0:
            return True

    # horizontal check
    for i in range(0, 5):
        sm_tmp = 0
        for char in 'BINGO':
            sm_tmp += bingo_card[char][i]
        if sm_tmp == 0:
            return True

    # diagonal check NW->SE
    sm_tmp = 0
    for i, char in enumerate('BINGO'):
        sm_tmp += bingo_card[char][i]
    if sm_tmp == 0:
        return True

    # diagonal check NE->SW
    sm_tmp = 0
    for i, char in enumerate('OGNIB'):
        sm_tmp += bingo_card[char][i]
    if sm_tmp == 0:
        return True

    return False


def main():
    bingo_card = ex138.create_bingo_card()
    bingo_card['G'] = [0, 0, 0, 0, 0]
    ex138.print_bingo_card(bingo_card)
    print(check_bingo_card_if_won(bingo_card))

    print()
    bingo_card = ex138.create_bingo_card()
    for char in 'BINGO':
        bingo_card[char][1] = 0
    ex138.print_bingo_card(bingo_card)
    print(check_bingo_card_if_won(bingo_card))

    print()
    bingo_card = ex138.create_bingo_card()
    for i, char in enumerate('BINGO'):
        bingo_card[char][i] = 0
    ex138.print_bingo_card(bingo_card)
    print(check_bingo_card_if_won(bingo_card))

    print()
    bingo_card = ex138.create_bingo_card()
    for i, char in enumerate('OGNIB'):
        bingo_card[char][i] = 0
    ex138.print_bingo_card(bingo_card)
    print(check_bingo_card_if_won(bingo_card))


if __name__ == '__main__':
    main()

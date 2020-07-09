import ex138
import ex139


def cross_number_bingo_card(num, bingo_card):
    for i in bingo_card:
        for j in range(0, 5):
            if bingo_card[i][j] == num:
                bingo_card[i][j] = 0

    return bingo_card


def main():
    bingo_card = ex138.create_bingo_card()
    ex138.print_bingo_card(bingo_card)
    print(ex139.check_bingo_card_if_won(bingo_card))

    for i in list(range(16, 31)):
        cross_number_bingo_card(i, bingo_card)
    ex138.print_bingo_card(bingo_card)
    print(ex139.check_bingo_card_if_won(bingo_card))


if __name__ == '__main__':
    main()

import ex138
import ex139
import ex139b


def play_bingo():
    from random import shuffle
    bingo_calls = list(range(1, 76))
    shuffle(bingo_calls)

    bingo_card = ex138.create_bingo_card()

    turns_to_win = 0
    while not ex139.check_bingo_card_if_won(bingo_card):
        bingo_card = ex139b.cross_number_bingo_card(bingo_calls[0], bingo_card)
        bingo_calls = bingo_calls[1:]
        turns_to_win += 1

    return turns_to_win


def main():
    turns_to_win_list = []
    game_num = int(1e3)
    for i in range(0, game_num):
        turns_to_win_list.append(play_bingo())

    print('games number:\t\t', game_num)
    print('min turns to win:\t', min(turns_to_win_list))
    print('max turns to win:\t', max(turns_to_win_list))
    print('mean turns to win:\t', sum(turns_to_win_list)/game_num)


main()

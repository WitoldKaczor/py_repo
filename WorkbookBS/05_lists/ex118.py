def create_deck(number_of_decks=1):
    card_values = [str(x) for x in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
    card_suits = ['s', 'h', 'd', 'c']

    deck = []
    for value in card_values:
        for suit in card_suits:
            deck.append(value + suit)

    return number_of_decks*deck


def shuffle_deck(deck):
    from random import randint

    shuffle_num = len(deck)*5
    for i in range(0, shuffle_num):
        pos1 = randint(0, 51)
        pos2 = randint(0, 51)
        deck[pos1], deck[pos2] = deck[pos2], deck[pos1]

    return deck


def main():
    deck = create_deck()
    print(deck)
    deck = shuffle_deck(deck)
    print(deck)


if __name__ == '__main__':
    main()

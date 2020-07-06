from ex118 import create_deck, shuffle_deck


def deal(number_of_hands, cards_per_hand, deck):
    if number_of_hands*cards_per_hand > len(deck):
        print('Invalid input')
        return

    cards_to_deal = deck[0:number_of_hands*cards_per_hand]
    remaining_cards = deck[number_of_hands*cards_per_hand:]

    ctr = 0
    hands = []
    for i in range(0, number_of_hands):
        hand = []
        for j in range(0+ctr, number_of_hands*cards_per_hand, number_of_hands):
            hand.append(cards_to_deal[j])

        hands.append(hand)
        ctr += 1

    return hands, remaining_cards


def main():
    deck = shuffle_deck(create_deck())
    hands, remaining_cards = deal(number_of_hands=4, cards_per_hand=5, deck=deck)
    print('Hands')
    print(hands)
    print()
    print('Remaining cards in dec')
    print(remaining_cards)


main()

def scrabble_score(word):
    for char in word:
        if not char.isalpha():
            print('Invalid input: not a word')
            return 0

    points_dict = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
                   2: ['D', 'G'],
                   3: ['B', 'C', 'M', 'P'],
                   4: ['F', 'H', 'V', 'W', 'Y'],
                   5: ['K'],
                   8: ['J', 'X'],
                   10: ['Q', 'Z']}

    word = word.upper()
    score_total = 0

    '''for char in word:
        for score in points_dict:
            if char in points_dict[score]:
                score_total += score'''

    for char in word:
        score_total += [score for score in points_dict if char in points_dict[score]][0]

    return score_total


def main():
    print(scrabble_score('hello'))
    print(scrabble_score('qabalistic'))
    print(scrabble_score('two words'))
    print(scrabble_score('Not32word'))


main()

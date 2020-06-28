while True:
    letter = input('Input a letter: ')

    if letter in 'aeiou':
        print(letter, 'is a vowel')
    elif letter == 'y':
        print(letter, 'is sometimes a vowel, sometimes a consonant')
    elif letter in 'bcdfghjklmnpqrstvwxz':
        print(letter, 'is a consonant')
    else:
        print(letter, 'is not a letter')

while True:
    word = input('Type a word: ')

    if word == word[::-1]:
        print('Word is a palindrome')
    else:
        print('Word is not a palindrome')

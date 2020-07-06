print('Input words (blank for quit)')
word = input()
word_set = {word}

while word != '':
    word = input()
    if word != '':
        word_set.add(word)

print(word_set)

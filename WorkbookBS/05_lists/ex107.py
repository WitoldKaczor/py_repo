print('Input words (blank for quit)')
word = input()
word_list = [word]

while word != '':
    word = input()
    if word not in word_list and word != '':
        word_list.append(word)

print(word_list)

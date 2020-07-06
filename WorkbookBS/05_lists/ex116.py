# text = input('Input a text: ')
text = 'Computer; science!'
print(text)

text = text.split()

for idx, word in enumerate(text):
    punctuation = ''
    is_capital = False
    if word[len(word) - 1] in ",.?-'!:;":
        punctuation = word[len(word) - 1]
        word = word[0:len(word) - 1]

    if word[0].isupper():
        is_capital = True

    if word[0] not in 'euioa':
        word_tmp1 = ''
        word_tmp2 = word

        for char in word:
            if char in 'euioa':
                break
            else:
                word_tmp1 += char
                word_tmp2 = word_tmp2.replace(char, '', 1)

        text[idx] = word_tmp2 + word_tmp1 + 'ay' + punctuation
    else:
        text[idx] = text[idx] + 'way' + punctuation

    if is_capital:
        text[idx] = text[idx].capitalize()

text_output = ''
for i in range(0, len(text)):
    text_output += text[i]
    if i != len(text):
        text_output += ' '

print(text_output)

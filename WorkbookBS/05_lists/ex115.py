# text = input('Input a text: ')
text = 'computer Think algorithm office'

text = text.lower().split()

for idx, word in enumerate(text):
    if word[0] not in 'euioa':
        word_tmp1 = ''
        word_tmp2 = word
        for char in word:
            if char in 'euioa':
                break
            else:
                word_tmp1 += char
                word_tmp2 = word_tmp2.replace(char, '', 1)

        text[idx] = word_tmp2 + word_tmp1 + 'ay'
    else:
        text[idx] += 'way'

print(text)

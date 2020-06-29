
shift = int(input('Input the shift for the cipher: '))
print('Input your message to encrypt')
txt = input()

txt_new = ''
for char in txt:
    if char.isalpha():
        if char.isupper():
            if ord(char)+shift > 90:
                char = chr(ord(char) + shift - 26)
            elif ord(char)+shift < 65:
                char = chr(ord(char) + shift + 26)
            else:
                char = chr(ord(char) + shift)
        else:  # char is lower
            if ord(char)+shift > 122:
                char = chr(ord(char) + shift - 26)
            elif ord(char) + shift < 97:
                char = chr(ord(char) + shift + 26)
            else:
                char = chr(ord(char) + shift)

    txt_new += char

print('Encrypted message:')
print(txt_new)

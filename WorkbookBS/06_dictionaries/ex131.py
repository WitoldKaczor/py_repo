def morse_code(message):
    morse_code_dict = {'a': '.-',
                       'b': '-...',
                       'c': '-.-.',
                       'd': '-..',
                       'e': '.',
                       'f': '..-.',
                       'g': '- -.',
                       'h': '....',
                       'i': '..',
                       'j': '.- - -',
                       'k': '-.-',
                       'l': '.-..',
                       'm': '- -',
                       'n': '-.',
                       'o': '- - -',
                       'p': '.- -.',
                       'q': '- -.-',
                       'r': '.-.',
                       's': '...',
                       't': '-',
                       'u': '..-',
                       'v': '...-',
                       'w': '.- -',
                       'x': '-..-',
                       'y': '-.- -',
                       'z': '- -..',
                       '0': '- - - - -',
                       '1': '.- - - -',
                       '2': '..---',
                       '3': '...- -',
                       '4': '....-',
                       '5': '.....',
                       '6': '-....',
                       '7': '- -...',
                       '8': '- - -..',
                       '9': '----.'}
    message_morse_code = ''

    message = message.lower()
    for char in message:
        if char not in morse_code_dict:
            continue
        else:
            message_morse_code += morse_code_dict[char] + '|'

    return message_morse_code


def main():
    print(morse_code('Hello, World!'))


main()

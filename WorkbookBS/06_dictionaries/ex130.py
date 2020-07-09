def key_presses(message):
    message = message.lower()

    phone_keys = {1: ['.', ',', '?', '!', ':'],
                  2: ['a', 'b', 'c'],
                  3: ['d', 'e', 'f'],
                  4: ['g', 'h', 'i'],
                  5: ['j', 'k', 'l'],
                  6: ['m', 'n', 'o'],
                  7: ['p', 'q', 'r', 's'],
                  8: ['t', 'u', 'v'],
                  9: ['w', 'x', 'y', 'z'],
                  0: [' ']}

    key_list = []
    for char in message:
        for key in phone_keys:
            if char in phone_keys[key]:
                for symbol in phone_keys[key]:
                    key_list.append(key)
                    if char == symbol:
                        break
    return key_list


def main():
    print(key_presses('Hello, World!'))


main()

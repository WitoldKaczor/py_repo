def count_unique_char(text):
    char_set = set()
    text = text.lower()

    for char in text:
        char_set.add(char)

    return len(char_set)


def main():
    print(count_unique_char('Hello, World!'))
    print(count_unique_char('zzz?'))


main()

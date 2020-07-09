def is_anagram(word1, word2):
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')
    char1 = []
    char2 = []

    for char in word1:
        char1.append(ord(char))

    for char in word2:
        char2.append(ord(char))

    char1.sort()
    char2.sort()

    return True if char1 == char2 else False


def main():
    print(is_anagram('Live', 'Evil'))
    print(is_anagram('William Shakespeare', 'I am a weakish speller'))
    print(is_anagram('test', 'tests'))


main()

def word_list(text):
    words = text.split()

    for idx, word in enumerate(words):
        if word[0] in ",.?-'!:;":
            words[idx] = word[1:]
        elif word[-1] in ",.?-'!:;":
            words[idx] = word[0:len(word)-1]

    words.remove('')

    return words


def main():
    text = "Examples - of contractions include: don't, isn't, and wouldn't."
    print(word_list(text))


if __name__ == '__main__':
    main()

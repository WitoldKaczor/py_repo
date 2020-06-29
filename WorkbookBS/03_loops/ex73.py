print("Input some phrases like 'Go, dog!', "
      "'Flee_to_me, remote Elf.' or 'some men interpret nine memos'")
while True:
    phrase = input()
    phrase_new = ''
    for char in phrase:
        if char.isalpha():
            phrase_new += char

    phrase_new = phrase_new.lower()

    if phrase_new == phrase_new[::-1]:
        print('Phrase is a palindrome')
    else:
        print('Phrase is not a palindrome')

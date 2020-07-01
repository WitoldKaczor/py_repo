def random_password():
    from random import randint
    pw_len = randint(7, 10)
    pw = ''
    for i in range(0, pw_len):
        pw += chr(randint(33, 126))
    return pw


def main():
    for i in range(0, 5):
        print(random_password())


if __name__ == '__main__':
    main()

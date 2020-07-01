def random_licence_plate():
    from random import randint
    if randint(0, 1) == 0:
        lp = chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) \
             + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
    else:
        lp = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) \
             + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90))
    return lp


def main():
    for i in range(0, 6):
        print(random_licence_plate())


if __name__ == '__main__':
    main()

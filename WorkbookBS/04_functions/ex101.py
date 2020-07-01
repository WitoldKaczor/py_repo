def reduce_fraction(num, den):
    if not isinstance(num, int) or not isinstance(den, int):
        print('Invalid input')
        return num, den

    d = min(abs(num), abs(den))
    while abs(num) % d != 0 or abs(den) % d != 0:
        d -= 1

    return num // d, den // d


def main():
    print(reduce_fraction(63, 3))
    print(reduce_fraction(55, 11))
    print(reduce_fraction(3.6, 2))


main()

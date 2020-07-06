from ex109 import proper_divisor


def is_perfect_number(num):
    if isinstance(num, int):
        if sum(proper_divisor(num)) == num:
            return True
        else:
            return False
    else:
        print(num, 'is not an integer')
        return


def main():
    perfect_numbers = []
    for n in range(1, int(1e4)):
        if is_perfect_number(n):
            perfect_numbers.append(n)
    print(perfect_numbers)


main()

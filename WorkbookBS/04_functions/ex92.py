def is_prime_number(num):
    if isinstance(num, int) and num >= 0:  # is positive integer
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        for divisor in range(2, num-1):
            if num % divisor == 0:
                return False
        else:
            return True


def main():
    for x in (0, 1, 2, 3, 5, 33, 121, 139):
        if is_prime_number(x):
            print(x, 'is a prime number')
        else:
            print(x, 'is not a prime number')


if __name__ == '__main__':
    main()

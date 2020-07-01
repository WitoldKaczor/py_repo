from ex92 import is_prime_number


def next_prime_number(num):
    num += 1
    while not is_prime_number(num):
        num += 1
    return num


def main():
    print(next_prime_number(3))
    print(next_prime_number(10))
    print(next_prime_number(121))
    print(next_prime_number(int(1e6)))


if __name__ == '__main__':
    main()

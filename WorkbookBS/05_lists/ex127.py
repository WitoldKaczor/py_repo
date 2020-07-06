def sieve_of_eratosthenes(limit=100):
    num_list = [x for x in range(2, limit+1)]

    for i in num_list:
        if i == 0:
            continue
        for j in range(2*i, limit+1, i):
            num_list[j-2] = 0

    return [x for x in num_list if x != 0]


def main():
    print(sieve_of_eratosthenes(int(1e3)))


main()

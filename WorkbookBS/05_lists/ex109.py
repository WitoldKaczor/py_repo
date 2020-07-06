def proper_divisor(num):
    if isinstance(num, int):
        pd_list = []
        for i in range(1, num):
            if num % i == 0:
                pd_list.append(i)
        return pd_list
    else:
        print(num, 'is not an integer')
        return num


def main():
    print(proper_divisor(5))
    print(proper_divisor(70))
    print(proper_divisor(60))

    pd_array = []
    for i in range(1, 100):
        pd_array.append(len(proper_divisor(i)))
    print('numbers in range (1..100) with most (', max(pd_array), ') proper divisors: ',
          [i+1 for i, x in enumerate(pd_array) if x == max(pd_array)], sep='')


if __name__ == '__main__':
    main()

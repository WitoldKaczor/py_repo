def count_in_range(num_list, num_min, num_max):
    if num_min > num_max:
        tmp = num_min
        num_min = num_max
        num_max = tmp

    ctr = 0
    for num in num_list:
        if num_min <= num <= num_max:
            ctr += 1
    return ctr


def main():
    print(count_in_range([0, 2, 1, -3, 2, 8, -1], 0, 1))
    print(count_in_range([0, 2, 1, -3, 2, 8, -1], 1, 0))
    print(count_in_range([-0.1, 22, 9.7, -3.2, 2.5, 1.8, 0.6, 3, -7], -1, +3))


main()

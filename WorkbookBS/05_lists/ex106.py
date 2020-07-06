def remove_extreme_values(data_list, n):
    if isinstance(n, int) and len(data_list) >= 4:
        data_list.sort()
        del data_list[-n:]
        del data_list[:n]
    elif not isinstance(n, int):
        print('n should be an integer: data not changed')
    else:
        print('list should have length of >4: data not changed')
    return data_list


def main():
    x = []
    for i in range(0, 10):
        x.append(i)

    print(x)
    print(remove_extreme_values(x, 3.6))
    print(remove_extreme_values(x[2:4], 2))
    print(remove_extreme_values(x, 3))


main()

def sublists_of_list(lst):
    n = len(lst)+1
    res = [[]]
    x = n
    while x > 1:
        for i in range(0, n+1-x):  # n+1-x = number of sublists of length x
            res.append(lst[i:i+x-1])
        x -= 1
    return res


def main():
    print(sublists_of_list([]))
    print(sublists_of_list([3]))
    print(sublists_of_list(['a', 'b']))
    print(sublists_of_list([1, 2, 3]))
    print(sublists_of_list([2.4, -1, 0, 3]))


main()

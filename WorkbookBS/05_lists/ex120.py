def is_sorted(num_list):
    num_list1 = num_list.copy()
    num_list1.sort()
    num_list2 = num_list.copy()
    num_list2.sort(reverse=True)

    if num_list == num_list1 or num_list == num_list2:
        return True
    else:
        return False


def main():
    x = [0, 2, 1, -3, 2, 8, -1]
    print(is_sorted(x))


main()

def is_sublist(larger_list, smaller_list):
    if len(smaller_list) > len(larger_list):
        return False, 0

    if smaller_list == larger_list:
        return True, 1

    if not smaller_list:
        return True, 1

    if smaller_list[0] in larger_list:
        idx_list = []
        for idx, item in enumerate(larger_list):
            if item == smaller_list[0]:
                idx_list.append(idx)
        # print(idx_list)

        ctr_sublist = 0
        for idx in idx_list:
            ctr_elem = 0
            for i in range(0, len(smaller_list)):
                if larger_list[idx+i] == smaller_list[i]:
                    ctr_elem += 1
            if ctr_elem == len(smaller_list):
                ctr_sublist += 1

        if ctr_sublist != 0:
            return True, ctr_sublist
        else:
            return False, 0

    else:
        return False, 0


def main():
    print(is_sublist([1, 2, 3, 4], [1, 2, 3, 4]))
    print(is_sublist([1, 2, 3, 4], []))
    print(is_sublist([1, 2, 3, 4], [1, 2, 3]))
    print(is_sublist([1, 2, 3, 4], [2, 3]))
    print(is_sublist([1, 2, 3, 4], [2, 4]))
    print(is_sublist([1, 2, 3, 4], [5]))
    print(is_sublist([1, 2, 3, 1, 4], [1, 4]))
    print(is_sublist([1, 2, 2, 1, 4], [2]))
    print(is_sublist([1, 4, 2, 1, 4], [1, 4]))


if __name__ == '__main__':
    main()

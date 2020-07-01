def reduce_measures(cups, table_spoons, tea_spoons):
    if not isinstance(cups, int) or not isinstance(table_spoons, int) or not isinstance(tea_spoons, int):
        print('Invalid input')
        return
    if cups < 0 or table_spoons < 0 or tea_spoons < 0:
        print('Invalid input')
        return

    while tea_spoons >= 3:
        table_spoons += 1
        tea_spoons -= 3

    while table_spoons >= 16:
        cups += 1
        table_spoons -= 16

    return cups, table_spoons, tea_spoons


def main():
    print(reduce_measures(0, 0, 59))
    print(reduce_measures(0, 14, 30))
    print(reduce_measures(0.5, 1, 0))
    print(reduce_measures(2, 2, -4))


main()

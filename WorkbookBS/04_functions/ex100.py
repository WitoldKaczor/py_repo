def days_in_month(month, year):
    if month < 1 or month > 12 or year < 0 or year > 9999:
        return -1

    if year % 400 == 0:
        leap_year = True
    elif year % 400 != 0 and year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False

    if month == 2:
        if leap_year:
            return 29
        else:
            return 28

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        return 30


def main():
    print(days_in_month(2, 2020))
    print(days_in_month(3, 1920))


if __name__ == '__main__':
    main()

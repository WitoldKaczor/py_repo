from ex100 import days_in_month


def is_magic_date(day, month, year):
    if day*month == year % 100:
        return True
    else:
        return False


def main():
    for year in range(1900, 2001):
        for month in range(1, 12):
            for day in range(1, days_in_month(month, year)+1):
                if is_magic_date(day, month, year):
                    print(day, month, year)


main()

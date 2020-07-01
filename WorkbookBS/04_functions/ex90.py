def is_integer(s):
    s = s.strip(' ')
    if len(s) >= 1 and s.lstrip('-+').isdigit():
        return True
    else:
        return False


def main():
    print(is_integer('   '))
    print(is_integer('  3 '))
    print(is_integer(' -1 '))
    print(is_integer(' +121 '))
    print(is_integer(' -3123 '))
    print(is_integer(' -11.3 '))
    print(is_integer(' +   '))


if __name__ == '__main__':
    main()

def precedence(s):
    if len(s) != 1:
        return -1
    if s == '+':
        return 1
    elif s == '*':
        return 2
    elif s == '^':
        return 3
    else:
        return -1


def main():
    operator = input('Input an operator: ')
    if precedence(operator) == -1:
        print('Not a valid operator')
    else:
        print('Valid operator', operator)


if __name__ == '__main__':
    main()

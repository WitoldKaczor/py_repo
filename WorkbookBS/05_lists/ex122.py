def break_into_tokens(expression):
    expression = expression.replace(' ', '')

    import re
    token_list = [i for i in re.split(r'(\d+|[+*/^()-]|\W)', expression) if i]

    return token_list


def main():
    x = 'a = 13*  5 + (3 -5)/2'
    print(x)
    print(break_into_tokens(x))


if __name__ == '__main__':
    main()

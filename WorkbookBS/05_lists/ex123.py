from ex122 import break_into_tokens


def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3


def infix_to_postfix(infix_list):
    operators = []
    postfix = []

    for token in infix_list:
        # If the token is an integer then
        # Add the token to the end of postfix
        if token.isdigit() or token.isalpha():
            postfix.append(token)
            # infix_list.append(infix_list.pop(infix_list.index(token)))

        # If the token is an operator then
            # While operators is not empty and the last item in operators is not an open parenthesis
                    #  and precedence(token) < precedence(last item in operators) do
                # Remove the last item from operators and add it to postfix
            # Add token to the end of operators
        if token in '-+*/^':
            while operators and operators[-1] != '(' and precedence(token) < precedence(operators[-1]):
                postfix.append(operators[-1])
                operators.pop()
            operators.append(token)

        # If the token is an open parenthesis then
            # Add token to the end of operators
        if token == '(':
            operators.append(token)

        # If the token is a close parenthesis then
            # While the last item in operators is not an open parenthesis do
                # Remove the last item from operators and add it to postfix
            # Remove the open parenthesis from operators
        if token == ')':
            while operators[-1] != '(':
                postfix.append(operators[-1])
                operators.pop()
            operators.pop()

    # While operators is not the empty list do
        # Remove the last item from operators and add it to postfix
    while operators:
        postfix.append(operators[-1])
        operators.pop()

    return postfix


def main():
    expr = '13 *  5 + (3 -5)/2'
    tokens = break_into_tokens(expr)
    print(infix_to_postfix(tokens))


if __name__ == '__main__':
    main()

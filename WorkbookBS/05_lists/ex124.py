from ex122 import break_into_tokens
from ex123 import infix_to_postfix


def evaluate_postfix(postfix):
    def apply_oper(left, right, oper):  # '-+*/^'
        if oper == '-':
            return left-right
        elif oper == '+':
            return left+right
        elif oper == '*':
            return left*right
        elif oper == '/':
            return left/right
        elif oper == '^':
            return left**right

    values = []
    # For each token in the postfix expression
    for token in postfix:
        # If the token is a number then
            # Convert it to an integer and add it to the end of values
        if token.isdigit():
            values.append(int(token))
        # Else
            # Remove an item from the end of values and call it right
            # Remove an item from the end of values and call it left
            # Apply the operator to left and right
            # Append the result to the end of values
        else:
            right_side = values[-1]
            values.pop()
            left_side = values[-1]
            values.pop()
            values.append(apply_oper(left_side, right_side, token))

    return values[0]


def main():
    expr = ' 3 *  5 + (  1 + 3  ) / 2 ^ 2'
    tokens = break_into_tokens(expr)
    postfix = infix_to_postfix(tokens)
    value = evaluate_postfix(postfix)

    print(expr)
    print(tokens)
    print(postfix)
    print(value)


if __name__ == '__main__':
    main()

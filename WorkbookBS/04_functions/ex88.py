def is_a_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if 2*max(a, b, c) - a - b - c < 0:
        return True
    else:
        return False


def main():
    print(is_a_triangle(-1, 1, 2))
    print(is_a_triangle(1, 0, 2))
    print(is_a_triangle(3, 4, 5))


main()

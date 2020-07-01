def string_center(string, width):
    if width < len(string):
        return string
    space_num = (width - len(string)) // 2
    return space_num*' ' + string + space_num*' '


def main():
    test_string = 'test'
    test_width = 20
    print(string_center(test_string, test_width))
    print(test_string.center(test_width))


main()

def hex2int(s):
    s = s.lower()
    for char in s:
        if not char.isdigit() and char not in 'abcdef':
            print('Invalid input')
            return

    num = 0
    ctr = 0
    s_back = s[::-1]
    for char in s_back:
        if char.isdigit():
            num += int(char) * 16**ctr
        else:
            num += (ord(char)-87) * 16**ctr
        ctr += 1
    return num


def int2hex(n):
    if not isinstance(n, int):
        print('Invalid input')
        return

    s = ''
    while n > 0:
        if n % 16 > 9:
            s += chr(n % 16 + 87)
        else:
            s += str(n % 16)
        n //= 16
    return s[::-1].upper()


def main():
    print(hex2int('211a'))  # 8474
    print(hex2int('100F'))  # 4111
    print(hex2int('-41'))  # invalid
    print(hex2int('5.37'))  # invalid

    print()

    print(int2hex(8474))  # 211A
    print(int2hex(4111))  # 100F
    print(int2hex(3.55))  # invalid
    print(int2hex(-42))  # invalid


if __name__ == '__main__':
    main()

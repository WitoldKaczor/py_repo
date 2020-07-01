def n2dec(num, base):
    if base < 2 or base > 16:
        print('Invalid base')
        return

    if base > 10:
        num = num.lower()
        for char in num:
            if not char.isdigit() and char not in 'abcdef'[0:base-10]:
                print('Invalid number')
                return
    else:
        for char in num:
            if not char.isdigit():
                print('Invalid number')
                return

    dec = 0
    ctr = 0
    num = num[::-1]
    for char in num:
        if char.isdigit():
            dec += int(char) * base**ctr
        else:
            dec += (ord(char)-87) * base**ctr
        ctr += 1
    return dec


def dec2n(num, base):
    if not isinstance(num, int):
        print('Invalid input')
        return

    s = ''
    while num > 0:
        if num % base > 9:
            s += chr(num % base + 87)
        else:
            s += str(num % base)
        num //= base
    return s[::-1].upper()


def main():
    for base in range(11, 17):
        print(n2dec('211a', base))
    print()

    for base in range(2, 10):
        print(n2dec('101', base))
    print()

    for base in range(2, 17):
        print(dec2n(3519, base))


main()

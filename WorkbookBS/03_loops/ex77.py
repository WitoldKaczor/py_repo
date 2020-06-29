from re import findall

num_bin = input('Input a binary number: ')

if len(num_bin) != len(findall('[01]', num_bin)):
    print('Invalid input')
else:
    ctr = 0
    num_dec = 0
    for char in num_bin[::-1]:
        num_dec += int(char) * 2**ctr
        ctr += 1

    print('The binary number', num_bin, 'equals the decimal number', num_dec)

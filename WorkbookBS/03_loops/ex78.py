num_dec = int(input('Input a positive integer: '))

if num_dec < 0:
    print('Only positive values allowed')
else:
    num_bin = ''
    num_tmp = num_dec
    ctr = 0
    while num_tmp > 1:
        num_bin += str(num_tmp % 2)
        num_tmp //= 2

    num_bin += '1'
    num_bin = num_bin[::-1]
    print('The decimal number', num_dec, 'equals the binary number', num_bin)

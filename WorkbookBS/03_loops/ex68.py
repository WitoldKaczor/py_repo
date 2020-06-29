import re

# even parity
while True:
    bits = input('Input 8 bits: ')
    if len(bits) != 8 or len(re.findall('[01]', bits)) != 8:
        print('Not a bits group!')
        continue

    if sum(int(digit) for digit in str(bits)) % 2 == 0:
        parity_bit = 0
    else:
        parity_bit = 1

    print('For', bits, 'the parity bit is', parity_bit)

num = int(input('Input a positive integer: '))

print('The prime factors of', num, 'are:')

if num < 0:
    print('Only positive numbers allowed')
else:
    fac = 2

    while num > 1:
        if num % fac == 0:
            num //= fac
            print(fac)
            fac = 2
        else:
            fac += 1

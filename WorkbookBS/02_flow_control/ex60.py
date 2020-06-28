# • Single number (1 to 36, 0, or 00)
# • Red versus Black
# • Odd versus Even (Note that 0 and 00 do not pay out for even)
# • 1 to 18 versus 19 to 36

from random import randint

print(5*'=', 'Roulette', 5*'=')

num = randint(-1, 36)

if num == -1:
    print('The spin resulted in 00 ...')
    print('Pay 00')
else:
    print('The spin resulted in ', num, '...', sep='')
    print('Pay', num)

if num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
    print('Pay Red')
elif num > 1:
    print('Pay Black')

if num != -1 and num != 0:
    if num % 2 == 0:
        print('Pay Even')
    else:
        print('Pay Odd')

if num in range(1, 19):
    print('Pay 1 to 18')
elif num in range(19, 37):
    print('Pay 19 to 36')

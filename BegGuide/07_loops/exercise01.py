number = int(input('Input an integer: '))

if number < 0:
    print('Number should be positive')
elif number == 0 or number == 1:
    print(number, '! = ', 1, sep='')
else:
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    print(number, '! = ', factorial, sep='')

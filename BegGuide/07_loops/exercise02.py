number = int(input('Input an integer: '))

if number < 2:
    print('Number should be greater than 2')
elif number == 2:
    print('2 is prime number')
else:
    for i in range(3, number+1):
        # print('i =', i)
        for j in range(2, i):
            # print('j =', j)
            if i % j == 0:
                break
        else:
            print(i, 'is prime number')

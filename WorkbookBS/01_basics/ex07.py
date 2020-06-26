num = int(input('Input a number: '))

if num < 1:
    print('Number has to be greater than 1')
else:
    result = num*(num+1)/2
    print('The sum of the integers from 1 to', num, 'equals', result)

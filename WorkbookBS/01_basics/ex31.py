num_input = input('Input a four-digit integer: ')
if len(num_input) > 4:
    print('Wrong input')
else:
    num = int(num_input)

    digit1 = num//1000
    num -= digit1*1000

    digit2 = num//100
    num -= digit2*100

    digit3 = num // 10
    num -= digit3 * 10

    digit4 = num

    print(digit1, '+', digit2, '+', digit3, '+', digit4, '=',
          digit1+digit2+digit3+digit4)

def median_of_three(a, b, c):
    max_num = max(a, b, c)
    min_num = min(a, b, c)
    median = a + b + c - min_num - max_num
    return median


num1 = float(input('Input first number: '))
num2 = float(input('Input second number: '))
num3 = float(input('Input third number: '))

print('median: %.2f' % median_of_three(num1, num2, num3))

# data_X = [1, 2, 3]
# data_Y = [1, 2.1, 2.9]

data_X = []
data_Y = []

print('Input data')
ctr = 0
while True:
    print('x', ctr, ' = ', sep='', end='')
    x = input()

    if x == '':
        break

    print('y', ctr, ' = ', sep='', end='')
    y = input()

    if y == '':
        y = '0'
        break

    data_X.append(float(x))
    data_Y.append(float(y))

    ctr += 1

# Calculation
n = len(data_X)
sumX = sum(data_X)
sumY = sum(data_Y)
meanX = sumX/n
meanY = sumY/n
sumXY = 0.0
sumXX = 0.0
for i in range(0, n):
    sumXY += data_X[i] * data_Y[i]
    sumXX += data_X[i] * data_X[i]

m = (sumXY - (sumX*sumY)/n) / (sumXX - (sumX**2)/n)
b = meanY - m * meanX

print()
print('Best Fit')
print('y = %.2f' % m, 'x + %.2f' % b, sep='')

print(5*'=', 'Average', 5*'=')
print('Input numbers for mean calculation')
print('To stop input and calculate enter 0')

num = 1
sm = 0.0
ctr = 0
while num != 0:
    num = int(input())
    sm += num
    if num != 0:
        ctr += 1

mean = sm / ctr
print('mean:', mean)

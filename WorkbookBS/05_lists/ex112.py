print('Input integers (blank for quit)')

num_list = []
while True:
    num = input()

    if num == '':
        break

    num_list.append(int(num))

mean = sum(num_list)/len(num_list)
average_list = []
above_list = []
below_list = []

for num in num_list:
    if num == mean:
        average_list.append(num)
    elif num > mean:
        above_list.append(num)
    else:
        below_list.append(num)

print('All numbers: ', num_list)
print('Average: %.2f' % mean)
print('Average numbers: ', average_list)
print('Numbers above average: ', above_list)
print('Numbers below average: ', below_list)

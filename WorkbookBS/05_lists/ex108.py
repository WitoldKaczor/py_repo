print('Input integers (blank for quit)')

zero_list = []
pos_list = []
neg_list = []

while True:
    num = input()

    if num == '':
        break

    if int(num) == 0:
        zero_list.append(int(num))
    elif int(num) < 0:
        neg_list.append(int(num))
    elif int(num) > 0:
        pos_list.append(int(num))


num_list = neg_list + zero_list + pos_list
print(num_list)

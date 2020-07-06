print('Input numbers to save in a sorted list (0 to quit)')
num = float(input())
num_list = [num]

while num != 0.0:
    num = float(input())
    if num != 0.0:
        num_list.append(num)

num_list.sort()
for number in num_list:
    print(number)

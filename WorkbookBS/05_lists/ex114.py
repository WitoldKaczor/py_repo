from random import choice

num_list = list(range(1, 50))
lottery = []

for i in range(0, 6):
    x = choice(num_list)
    lottery.append(x)
    num_list.remove(x)

lottery.sort()
print(lottery)

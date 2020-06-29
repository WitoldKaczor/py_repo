print('Input age of all visitors')

total_cost = 0.0

while True:
    age = input()
    if age == '':
        break

    age = int(age)
    if age < 3:
        total_cost += 0.00
    elif 3 <= age <= 12:
        total_cost += 14.00
    elif 65 <= age:
        total_cost += 18.00
    else:
        total_cost += 23.00

print('Total cost for the group:  $%.2f' % total_cost)

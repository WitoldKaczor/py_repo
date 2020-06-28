while True:
    bill = int(input('Input a denomination: '))

    bills_dict = {1: 'George Washington',
                  2: 'Thomas Jefferson',
                  5: 'Abraham Lincoln',
                  10: 'Alexander Hamilton',
                  20: 'Andrew Jackson',
                  50: 'Ulysses S. Grant',
                  100: 'Benjamin Franklin'}

    if bill in bills_dict:
        print(bills_dict[bill], ' is printed on the ', bill, '$ note', sep='')
    else:
        print('There is no such denomination')

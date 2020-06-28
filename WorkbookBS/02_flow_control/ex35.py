human_years = int(input('Human years: '))

if human_years < 0:
    print('Only positive values valid')
elif human_years < 3:
    dog_years = 10.5 * human_years
    if human_years == 1:
        print(human_years, 'human year is', dog_years, 'dog years')
    else:
        print(human_years, 'human years are', dog_years, 'dog years')
else:
    dog_years = 10.5 * 2 + 4 * (human_years-2)
    print(human_years, 'human years are', dog_years, 'dog years')

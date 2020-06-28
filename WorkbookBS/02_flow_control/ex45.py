while True:
    position = input('input chess field: ')

    if len(position) != 2:
        print('Invalid input')
        continue
    elif position.lower()[0] not in 'abcdefgh' or position[1] not in '12345678':
        if position.lower()[1] in 'abcdefgh' and position[0] in '12345678':
            position = position[::-1]
        else:
            print('Invalid input')
            continue

    if position[0] in 'aceg' and int(position[1]) % 2 == 1:
        print('field', position, 'is black')
    elif position[0] in 'bdfh' and int(position[1]) % 2 == 0:
        print('field', position, 'is black')
    else:
        print('field', position, 'is white')

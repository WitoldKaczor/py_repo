def reverse_lookup(dictionary, value):
    key_list = []
    for key in dictionary:
        if dictionary[key] == value:
            key_list.append(key)

    return key_list


def main():
    cities = {'Wales': 'Cardiff',
              'England': 'London',
              'Great Britain': 'London',
              'Scotland': 'Edinburgh',
              'Northern Ireland': 'Belfast',
              'Ireland': 'Dublin'}

    print(reverse_lookup(cities, 'Dublin'))
    print(reverse_lookup(cities, 'Paris'))
    print(reverse_lookup(cities, 'London'))


if __name__ == '__main__':
    main()

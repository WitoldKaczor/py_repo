# exercise01
str_commas = 'Denyse,Marie,Smith,21,London,UK'
print(str_commas.replace(',', ' '))

# exercise02
first_str = input('Input first string: ')
second_str = input('Input second string: ')
new_string = first_str + ' ' + second_str
print(new_string)
print('Length of the new string is', len(new_string))
new_string = new_string.upper()
print(new_string)
if new_string.lower().find('albus') == -1:
    print('New string does not contain "Albus"')
else:
    print('New string contains "Albus"')

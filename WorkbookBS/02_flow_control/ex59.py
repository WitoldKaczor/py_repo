# old: three uppercase letters followed by three numbers
# new: four numbers followed by three uppercase letters

lic_plate = input('Input a licence plate: ')

if len(lic_plate) != 6 and len(lic_plate) != 7:
    print('Invalid licence plate')
elif len(lic_plate) == 6 and lic_plate[0:3].isalpha() and lic_plate[0:3].isupper() and lic_plate[3:6].isdigit():
    print('Valid older licence plate')
elif len(lic_plate) == 7 and lic_plate[0:4].isdigit() and lic_plate[4:7].isalpha() and lic_plate[4:7].isupper():
    print('Valid newer licence plate')
else:
    print('Invalid licence plate')

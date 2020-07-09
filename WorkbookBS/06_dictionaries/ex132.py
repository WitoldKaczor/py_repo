def province(postal_code):
    province_dict = {'A': 'Newfoundland',
                     'B': 'Nova Scotia',
                     'C': 'Prince Edward Island',
                     'E': 'New Brunswick',
                     'G': 'Quebec',
                     'H': 'Quebec',
                     'J': 'Quebec',
                     'K': 'Ontario',
                     'L': 'Ontario',
                     'M': 'Ontario',
                     'N': 'Ontario',
                     'P': 'Ontario',
                     'R': 'Manitoba',
                     'S': 'Saskatchewan',
                     'T': 'Alberta',
                     'V': 'British Columbia',
                     'X': ['Nunavut', 'Northwest Territories'],
                     'Y': 'Yukon'}

    postal_code = postal_code.upper().replace(' ', '')
    if len(postal_code) != 6:
        print('Invalid input')
        return
    elif not [postal_code[i].isalpha() and postal_code[i+1].isdigit() for i in range(0, 6, 2)]:
        print('Invalid input')
        return
    else:
        if postal_code[0] not in province_dict:
            print('Invalid input, no province with code', postal_code[0].upper())
            return
        else:
            area = ('rural' if postal_code[1] == 0 else 'urban')
            if postal_code[0] != 'X':
                print('Postal code', postal_code, 'is from', area, 'area of', province_dict[postal_code[0]])
            else:
                print('Postal code', postal_code, 'is from', area, 'area of',
                      province_dict[postal_code[0]][0], 'or', province_dict[postal_code[0]][1])
            return


def main():
    province('T2N1N4 T2N')
    province('T2N 1N4')
    province('X0A1B2')


main()

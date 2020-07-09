def write_out_number(num):
    num_string = ''
    if not (isinstance(num, int) and num > 0):
        print('Invalid input')
        return

    upto20_dict = {1: 'one',
                   2: 'two',
                   3: 'three',
                   4: 'four',
                   5: 'five',
                   6: 'six',
                   7: 'seven',
                   8: 'eight',
                   9: 'nine',
                   10: 'ten',
                   11: 'eleven',
                   12: 'twelve',
                   13: 'thirteen',
                   14: 'fourteen',
                   15: 'fifteen',
                   16: 'sixteen',
                   17: 'seventeen',
                   18: 'eighteen',
                   19: 'nineteen'}
    tens_dict = {2: 'twenty',
                 3: 'thirty',
                 4: 'forty',
                 5: 'fifty',
                 6: 'sixty',
                 7: 'seventy',
                 8: 'eighty',
                 9: 'ninety'}

    if num > 99:
        num_string += upto20_dict[num//100] + ' hundred '
        num -= (num // 100) * 100

    if 0 < num < 20:
        num_string += upto20_dict[num]
    elif num > 20:
        num_string += tens_dict[num//10] + ' '
        num -= (num // 10) * 10
        num_string += upto20_dict[num]

    print(num_string)
    return


def main():
    write_out_number(-2)
    write_out_number(4.5)
    write_out_number(0)
    write_out_number(4)
    write_out_number(200)
    write_out_number(116)
    write_out_number(24)
    write_out_number(678)


main()

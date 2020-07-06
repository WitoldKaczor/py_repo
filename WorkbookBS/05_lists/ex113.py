def list_formatting(item_list):
    str_frmtd = ''
    for idx, item in enumerate(item_list):
        if idx == 0:
            str_frmtd += item
        if idx == len(item_list)-1:
            str_frmtd += ' and ' + item
        else:
            str_frmtd += ', ' + item

    return str_frmtd


def main():
    item_list = ['apples', 'oranges', 'bananas', 'lemons', 'mangoes']
    print(list_formatting(item_list))


main()

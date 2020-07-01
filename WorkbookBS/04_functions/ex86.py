from ex85 import ordinal_numbers


def twelve_days_of_christmas(verse_num):
    if verse_num < 1 or 12 < verse_num:
        return ''
    else:
        verse = 'On the ' + ordinal_numbers(verse_num) \
                + ' day of Christmas\nmy true love sent to me:\n'
        if verse_num == 1:
            verse += 'A partridge in a pear tree.'
        else:
            if verse_num == 12:
                verse += 'Twelve drummers drumming,\n'
            if verse_num >= 11:
                verse += 'Eleven pipers piping,\n'
            if verse_num >= 10:
                verse += 'Ten lords a-leaping,\n'
            if verse_num >= 9:
                verse += 'Nine ladies dancing,\n'
            if verse_num >= 8:
                verse += 'Eight maids a-milking,\n'
            if verse_num >= 7:
                verse += 'Seven swans a-swimming,\n'
            if verse_num >= 6:
                verse += 'Six geese a-laying,\n'
            if verse_num >= 5:
                verse += 'Five gold rings,\n'
            if verse_num >= 4:
                verse += 'Four calling birds,\n'
            if verse_num >= 3:
                verse += 'Three French hens,\n'
            if verse_num >= 2:
                verse += 'Two turtle doves,\n'
            verse += 'And a partridge in a pear tree.'
        return verse


def main():
    num = int(input('Input verse number: '))
    print(twelve_days_of_christmas(num))


main()

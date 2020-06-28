BASE_CHARGE = 15.0
MINUTES_INCLUDED = 50
TXT_MSG_INCLUDED = 50
ADD_MINUTE_COST = 0.25
ADD_TXT_MSG_COST = 0.15
CHARGE_911 = 0.44
SALES_TAX = 0.05

minutes = int(input('Number of minutes: '))
txt_msgs = int(input('Number of text messages: '))

if minutes < 0 or txt_msgs < 0:
    print('Invalid input')
else:
    left_padding = '{:<20}'
    right_padding = '{:>10.2f}$'
    print()
    print(5*'=', 'Cell Phone Bill', 5*'=')

    # base charge
    print(left_padding.format('Base charge'), right_padding.format(BASE_CHARGE))
    total_charge = BASE_CHARGE

    # additional minutes
    if minutes-MINUTES_INCLUDED > 0:
        print(left_padding.format('Additional minutes'),
              right_padding.format((minutes-MINUTES_INCLUDED)*ADD_MINUTE_COST))
        total_charge += (minutes-MINUTES_INCLUDED)*ADD_MINUTE_COST

    # additional text messages
    if txt_msgs-TXT_MSG_INCLUDED > 0:
        print(left_padding.format('Additional text messages'),
              right_padding.format((txt_msgs-TXT_MSG_INCLUDED)*ADD_TXT_MSG_COST))
        total_charge += (txt_msgs-TXT_MSG_INCLUDED)*ADD_TXT_MSG_COST

    # 911 fee
    print(left_padding.format('The 911 fee'), right_padding.format(CHARGE_911))
    total_charge += CHARGE_911

    # tax
    tax = total_charge*SALES_TAX
    print(left_padding.format('Sales Tax'), right_padding.format(tax))
    total_charge += tax

    # total charge
    print()
    print(left_padding.format('TOTAL'), right_padding.format(total_charge))

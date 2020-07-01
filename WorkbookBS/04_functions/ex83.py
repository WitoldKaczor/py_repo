def shipping_price(item_num):
    if item_num < 0:
        print('only non-negative numbers allowed')
        return 0
    elif item_num == 0:
        return 0
    else:
        return 10.95 + 2.95*(item_num-1)


print('${:.2f}'.format(shipping_price(0)))
print('${:.2f}'.format(shipping_price(1)))
print('${:.2f}'.format(shipping_price(2)))
print('${:.2f}'.format(shipping_price(10)))
print('${:.2f}'.format(shipping_price(-1)))

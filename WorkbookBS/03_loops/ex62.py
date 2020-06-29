DISCOUNT_RATE = 0.6

price_list = [4.95, 9.95, 14.95, 19.95, 24.95]

print('{:^20}'.format('Original price'),
      '{:^20}'.format('Discount'),
      '{:^20}'.format('New price'))

for price in price_list:
    print('{:^20.2f}'.format(price),
          '{:^20.2f}'.format(price*DISCOUNT_RATE),
          '{:^20.2f}'.format(price*(1-DISCOUNT_RATE)))

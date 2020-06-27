PRICE_LOAF = 3.49
loaves = int(input('number of bread loaves: '))

normal_price = PRICE_LOAF*loaves
discount = normal_price*0.6
total_price = normal_price-discount
print('{:<15}'.format('Normal price'), '{:>10.2f}$'.format(normal_price))
print('{:<15}'.format('Discount'), '{:>10.2f}$'.format(discount))
print('{:<15}'.format('Total price'), '{:>10.2f}$'.format(total_price))

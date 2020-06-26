num_small_bottles = int(input('Number of small bottles: '))
num_big_bottles = int(input('Number of big bottles: '))

deposit_cent = num_small_bottles*10 + num_big_bottles*25
print('Refund: {:.2f}'.format(deposit_cent/100), '$', sep='')

print(5*'=', 'Temperature conversion', 5*'=')

padding_width_header = '{:>10}'
padding_width_table = '{:>10.0f}'
print(padding_width_header.format('T in °C'), padding_width_header.format('T in °F'))
for T in range(0, 110, 10):
    print(padding_width_table.format(T), padding_width_table.format((T * 9/5) + 32))

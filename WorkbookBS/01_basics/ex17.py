SPEC_HEAT_CAPACITY = 4.186
DOLLAR_PER_KWH = 0.089

temp_change_K = float(input('Temperature change in °C / K: '))
mass_g = float(input('Water mass in g: '))

energy = mass_g * SPEC_HEAT_CAPACITY * temp_change_K
energy_cost = energy * DOLLAR_PER_KWH * 2.77778e-7

print('Amount of energy: {:.2f} J'.format(energy))
print('Cost of energy: {:.2f} $'.format(energy_cost))

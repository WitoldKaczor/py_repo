print(5*'-', 'Pressure Unit Converter', 5*'-')
p_kPa = float(input('Pressure in kPa: '))

p_psi = p_kPa * 0.145038
p_mmHg = p_kPa * 7.50062
p_atm = p_kPa * 0.00986923

print('{:.2f} kPa = '.format(p_kPa), end='')
print('{:.2f} psi = '.format(p_psi), end='')
print('{:.2f} mmHg = '.format(p_mmHg), end='')
print('{:.2f} atm'.format(p_atm))

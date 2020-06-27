GAS_CONST = 8.314  # J / (mol K)

temperature = 20 + 273.15  # K
volume = 12 * 1e-3  # m3
pressure = 2e7  # Pa

mol_amount = (pressure * volume) / (GAS_CONST * temperature)  # mol
print('{:.2f}'.format(mol_amount))

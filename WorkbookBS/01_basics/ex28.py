print(5*'-', 'Wind Chill Index', 5*'-')
T = float(input('air temperature in °C: '))
v = float(input('wind speed in km/h: '))

if T > 10 or v <= 4.8:
    print('Formula only valid for T ≤ 10°C and v > 4.8km/h !')
else:
    WCI = 13.12 + 0.6215*T - 11.37*v**0.16 + 0.3965*T*v**0.16
    print('wind chill index equals {:.2f}'.format(WCI))

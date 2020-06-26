KM_TO_MILE = 1.609
LITRE_TO_GALLON = 4.546

eff_L100km = float(input('fuel efficiency in L/100km: '))
eff_mpg = (1/eff_L100km)*100*LITRE_TO_GALLON/KM_TO_MILE
print(eff_L100km, 'L per 100km = {:.2f}'.format(eff_mpg), 'miles per gallon')

height_cm = float(input('height in centimeters: '))
weight_kg = float(input('weight in kilograms: '))

bmi = weight_kg / (height_cm/100)**2
print('bmi equals {:.2f}'.format(bmi))

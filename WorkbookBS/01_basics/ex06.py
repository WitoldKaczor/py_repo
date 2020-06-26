TAX_PERCENT = 10
TIP_PERCENT = 18

meal_cost = float(input('Meal price: '))
tax = meal_cost*TAX_PERCENT/100
tip = meal_cost*TIP_PERCENT/100
cost_total = meal_cost + tax + tip

print('To pay: {:.2f}'.format(cost_total), '$')

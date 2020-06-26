num_widget = int(input('Number of widgets: '))
num_gizmo = int(input('Number of gizmos: '))

weight_total = num_widget*75 + num_gizmo*112
print('Total weight of the order equals {:.3f}'.format(weight_total/1000), 'kg')

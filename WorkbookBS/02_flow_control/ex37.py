num_side = int(input('Input number of sides (3..10): '))

if num_side < 3 or num_side > 10:
    print('Invalid sides number')
else:
    shape_dict = {3: 'triangle',
                  4: 'rectangle',
                  5: 'pentagon',
                  6: 'hexagon',
                  7: 'heptagon',
                  8: 'octagon',
                  9: 'nonagon',
                  10: 'decagon'}

    shape_name = shape_dict[num_side]

    print('a shape with', num_side, 'sides is called', shape_name)

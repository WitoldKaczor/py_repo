from math import sqrt

GRAVITY_CONST = 9.8

height = float(input('Height from which the object is dropped in meters: '))

v_final_kmh = sqrt(2 * GRAVITY_CONST * height) * 3.6

print('Object hits the ground with {:.2f} km/h'.format(v_final_kmh))

dist_km = float(input('Distance in km: '))
if dist_km < 0:
    print('Distance cannot be negative!')
else:
    dist_mi = dist_km / 0.6214
    print(dist_km, 'km ≈', '{:.2f}'.format(dist_mi), 'miles')

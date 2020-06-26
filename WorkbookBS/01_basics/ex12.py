import math

EARTH_RADIUS = 6371.01

print('Latitude (-90..+90): + for North, - for South')
print('Longitude (-180..+180): + for East, - for West')

# user input
lat1 = float(input('First point, latitude in degrees: '))
lon1 = float(input('First point, longitude in degrees: '))
lat2 = float(input('Second point, latitude in degrees: '))
lon2 = float(input('Second point, longitude in degrees: '))

# limits check
if not -90 <= lat1 <= 90 or not -90 <= lat2 <= 90:
    print('Wrong input')
elif not -180 <= lon1 <= 180 or not -180 <= lon2 <= 180:
    print('Wrong input')
else:
    # conversion to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # calculation and output
    dist = EARTH_RADIUS * math.acos(
            math.sin(lat1) * math.sin(lat2)
            + math.cos(lat1) * math.cos(lat2) * math.cos(lon1-lon2))

    print(dist)

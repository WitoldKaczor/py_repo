def taxi_fare(distance_km):
    if distance_km < 0:
        print('only non-negative distances allowed')
        return 0
    else:
        base_fare = 4.00
        fare_per_km = 0.25 / (140/1000)
        total_fare = base_fare + fare_per_km*distance_km
        return total_fare


print('${:.2f}'.format(taxi_fare(1.0)))
print('${:.2f}'.format(taxi_fare(2.0)))
print('${:.2f}'.format(taxi_fare(10.0)))
print('${:.2f}'.format(taxi_fare(-3.0)))

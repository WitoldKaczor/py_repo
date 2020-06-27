int1 = int(input('First integer: '))
int2 = int(input('Second integer: '))
int3 = int(input('Third integer: '))

int_min = min(int1, int2, int3)
int_max = max(int1, int2, int3)
int_mid = int1 + int2 + int3 - int_min - int_max

print('Sorted numbers:', int_min, int_mid, int_max)

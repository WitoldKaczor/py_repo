def is_prime(num, i=2):
    # no negative numbers allowed
    if num < 0:
        print('Only non-negative numbers allowed')
        return False

    # 2 is prime number, 0 and 1 are not
    if num <= 2:
        return True if num == 2 else False

    # number can be divided without remaining -> not prime num
    if num % i == 0:
        return False

    # all of the divisors checked -> prime num
    if i == num - 1:
        return True

    # recursion, other divisors
    return is_prime(num, i + 1)


print('is_prime(1):', is_prime(1))  # False
print('is_prime(2):', is_prime(2))  # True
print('is_prime(3):', is_prime(3))  # True
print('is_prime(7):', is_prime(7))  # True
print('is_prime(9):', is_prime(9))  # False
print('is_prime(15):', is_prime(15))  # False
print('is_prime(31):', is_prime(31))  # True
print('is_prime(223):', is_prime(223))  # True

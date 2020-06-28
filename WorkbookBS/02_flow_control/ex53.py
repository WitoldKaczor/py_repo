while True:
    rating = float(input('Input rating: '))
    tol = 1e-3  # because of floating point

    if rating < 0.0-tol:
        print('Invalid rating')
    elif 0.0-tol < rating < 0.0+tol:
        print('Unacceptable performance')
        print('The amount of the employee’s raise: %.2f' % 0)
    elif 0.0+tol < rating < 0.4-tol:
        print('Invalid rating')
    elif 0.4-tol < rating < 0.4+tol:
        print('Acceptable performance')
        print('The amount of the employee’s raise: %.2f' % (2400*0.4))
    elif 0.4+tol < rating < 0.6-tol:
        print('Invalid rating')
    else:  # rating >= 0.6
        print('Meritorious performance')
        print('The amount of the employee’s raise: %.2f' % (2400 * rating))

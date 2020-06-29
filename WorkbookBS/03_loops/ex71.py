while True:
    x = float(input('Input a number: '))
    if x < 0:
        print('Only positive numbers allowed')
        continue

    TOLERANCE = 1e-10

    result = x / 2
    ctr = 0
    while abs(result*result - x) > TOLERANCE:
        result = (result + x/result) / 2
        ctr += 1

    print('sqr(%.2f' % x, ') = %.5f' % result, '  (in ', ctr,
          ' iterations, with tolerance = ', TOLERANCE, ')', sep='')

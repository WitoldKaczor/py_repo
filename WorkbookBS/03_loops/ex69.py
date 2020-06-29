APPROX_NUM = 20

pi_approx = 3
for i in range(1, APPROX_NUM+1):
    n = i + 2
    if i % 2 == 1:
        pi_approx += 4 / ((n-1)*(n)*(n+1))
    else:
        pi_approx -= 4 / ((n-1)*(n)*(n+1))

print('π ≈', pi_approx)

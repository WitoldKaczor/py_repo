def pascal_triangle_row(num):
    # no negative numbers allowed
    if num < 0:
        print('Only non-negative numbers allowed!')
        return -1

    if num == 0:
        return 1

    arr = []
    for i in range(0, num+1):
        if i == 0 or i == num:
            arr.append(1)
        else:
            arr_tmp = pascal_triangle_row(num - 1)
            arr.append(arr_tmp[i - 1] + arr_tmp[i])
    return arr


def pascal_triangle(num):
    for i in range(0, num + 1):
        print(pascal_triangle_row(i))


pascal_triangle(7)

# print(pascal_triangle_row(0))
# print(pascal_triangle_row(1))
# print(pascal_triangle_row(2))
# print(pascal_triangle_row(3))
# print(pascal_triangle_row(4))

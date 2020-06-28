# A+ 4.0
# A 4.0
# A− 3.7
# B+ 3.3
# B 3.0
# B− 2.7
# C+ 2.3
# C 2.0
# C− 1.7
# D+ 1.3
# D 1.0
# F 0

while True:
    grade = input('Input descriptive grade: ')
    grade = grade.lower()

    if len(grade) != 1 and len(grade) != 2:
        print('Invalid input')
    elif grade[0] not in 'abcdf':
        print('Invalid input')
    elif len(grade) == 2 and grade[1] not in '+-':
        print('Invalid input')
    elif grade[0] == 'f' and len(grade) == 2:
        print('Invalid input')
    elif grade == 'd-':
        print('Invalid input')
    else:
        if grade == 'a+' or grade == 'a':
            grade_num = 4.0
        elif grade == 'a-':
            grade_num = 3.7
        elif grade == 'b+':
            grade_num = 3.3
        elif grade == 'b':
            grade_num = 3.0
        elif grade == 'b-':
            grade_num = 2.7
        elif grade == 'c+':
            grade_num = 2.3
        elif grade == 'c':
            grade_num = 2.0
        elif grade == 'c-':
            grade_num = 1.7
        elif grade == 'd+':
            grade_num = 1.3
        elif grade == 'd':
            grade_num = 1.0
        else:  # 'f'
            grade_num = 0.0

        print('Grade %s is equivalent to %.1f' % (grade.upper(), grade_num))

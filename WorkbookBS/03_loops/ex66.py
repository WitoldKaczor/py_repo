print('Input descriptive grades to calculate average (blank line to quit)')

sm = 0.0
ctr = 0

while True:
    grade = input()
    if grade == '':
        break
    grade = grade.lower()

    if len(grade) != 1 and len(grade) != 2:
        print(grade, 'is invalid input, try again')
    elif grade[0] not in 'abcdf':
        print(grade, 'is invalid input, try again')
    elif len(grade) == 2 and grade[1] not in '+-':
        print(grade, 'is invalid input, try again')
    elif grade[0] == 'f' and len(grade) == 2:
        print(grade, 'is invalid input, try again')
    elif grade == 'd-':
        print(grade, 'is invalid input, try again')
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

        sm += grade_num
        ctr += 1

mean = sm / ctr
print('grade average: %.2f' % mean)

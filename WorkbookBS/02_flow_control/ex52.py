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
    grade_num = float(input('Input numeric grade: '))
    tol = 1e-3

    if grade_num > 4.0+tol or grade_num < 0.0-tol:
        print('Invalid input')
    else:
        if 4.0-tol <= grade_num <= 4.0+tol:
            grade = 'A+'
        elif 3.7 < grade_num <= 4.0-tol:
            grade = 'A'
        elif 3.3 < grade_num <= 3.7:
            grade = 'A-'
        elif 3.0 < grade_num <= 3.3:
            grade = 'B+'
        elif 2.7 < grade_num <= 3.0:
            grade = 'B'
        elif 2.3 < grade_num <= 2.7:
            grade = 'B-'
        elif 2.0 < grade_num <= 2.3:
            grade = 'C+'
        elif 1.7 < grade_num <= 2.0:
            grade = 'C'
        elif 1.3 < grade_num <= 1.7:
            grade = 'C-'
        elif 1.0 < grade_num <= 1.3:
            grade = 'D+'
        elif 0.0+tol < grade_num <= 1.0:
            grade = 'D'
        else:
            grade = 'F'

        print('Grade %.1f is equivalent to %s' % (grade_num, grade))

from ex94 import random_password


def is_password_good(pw):
    if len(pw) < 8:
        return False

    ctr_lower = 0
    ctr_upper = 0
    ctr_num = 0
    for char in pw:
        if char.isupper():
            ctr_upper += 1
        if char.islower():
            ctr_lower += 1
        if char.isdigit():
            ctr_num += 1

    if ctr_lower >= 1 and ctr_upper >= 1 and ctr_num >= 1:
        return True
    else:
        return False


def main():
    for i in range(0, 5):
        rand_pw = random_password()
        if is_password_good(rand_pw):
            print(rand_pw, '\tis a good password')
        else:
            print(rand_pw, '\tis NOT a good password')


if __name__ == '__main__':
    main()

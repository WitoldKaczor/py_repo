def random_good_password():
    from ex94 import random_password
    from ex96 import is_password_good
    attempts = 0
    pw = ''
    while not is_password_good(pw):
        pw = random_password()
        attempts += 1
    return pw, attempts


def main():
    for i in range(0, 5):
        password, attempts = random_good_password()
        if attempts == 1:
            print(password, '\t(in', attempts, 'attempt)')
        else:
            print(password, '\t(in', attempts, 'attempts)')


main()

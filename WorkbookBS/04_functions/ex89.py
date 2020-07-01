def text_corr(s):
    s_corr = s.replace(' i ', ' I ')

    s_corr = s_corr[0].upper() + s_corr[1:len(s_corr)]

    for idx, char in enumerate(s_corr):
        if char in '.!?' and idx != len(s_corr)-1:
            s_corr = s_corr[0:idx+2] + s_corr[idx+2].upper() + s_corr[idx+3:len(s_corr)]

    return s_corr


def main():
    s_test = 'what time do i have to be there? what’s the address?'
    print(s_test)
    print(text_corr(s_test))


main()

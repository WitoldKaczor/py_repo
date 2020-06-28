while True:
    freq = float(input('Input frequency in Hz: '))
    tol = 2.0

    if 261.63-tol < freq < 261.63+tol:
        print('Frequency 261.63 Hz corresponds to the note C4')
    elif 293.66-tol < freq < 293.66+tol:
        note = 'D4'
        print('Frequency 293.66 Hz corresponds to the note D4')
    elif 329.63-tol < freq < 329.63+tol:
        note = 'E4'
        print('Frequency 329.63 Hz corresponds to the note E4')
    elif 349.23-tol < freq < 349.23+tol:
        note = 'F4'
        print('Frequency 349.23 Hz corresponds to the note F4')
    elif 392.00-tol < freq < 392.00+tol:
        note = 'G4'
        print('Frequency 392.00 Hz corresponds to the note G4')
    elif 440.00-tol < freq < 440.00+tol:
        note = 'A4'
        print('Frequency 440.00 Hz corresponds to the note A4')
    elif 493.88-tol < freq < 493.88+tol:
        note = 'B4'
        print('Frequency 493.88 Hz corresponds to the note B4')
    else:
        print('Frequency {:.2f}'.format(freq), 'Hz does not correspond to any of the known notes')

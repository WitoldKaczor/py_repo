while True:
    note = input('Input note: ')

    if len(note) != 2 or note.lower()[0] not in 'abcdefg' or note[1] not in '012345678':
        print('Not a note')
    else:
        note = note.upper()
        note_dict = {'C4': 261.63,
                     'D4': 293.66,
                     'E4': 329.63,
                     'F4': 349.23,
                     'G4': 392.00,
                     'A4': 440.00,
                     'B4': 493.88}
        if note[1] == '4':
            freq = note_dict[note]
        else:
            freq = note_dict[note[0]+'4'] * 2**(int(note[1])-4)

        print('note', note, 'corresponds to frequency of {:.2f} Hz'.format(freq))

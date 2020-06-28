while True:
    sound_level = int(input('Input a sound level in dB: '))

    if sound_level < 0:
        print('Only positive values valid')
    elif sound_level > 130:
        print(sound_level, 'dB is louder than jackhammer')
    elif sound_level == 130:
        print(sound_level, 'dB is as loud as a jackhammer')
    elif sound_level > 106:
        print(sound_level, 'dB is louder than gas lawnmower but quieter than jackhammer')
    elif sound_level == 106:
        print(sound_level, 'dB is as loud as gas lawnmower')
    elif sound_level > 70:
        print(sound_level, 'dB is louder than alarm clock but quieter than gas lawnmower')
    elif sound_level == 70:
        print(sound_level, 'dB is as loud as alarm clock')
    elif sound_level > 40:
        print(sound_level, 'dB is louder than quiet room but quieter than alarm clock')
    elif sound_level == 40:
        print(sound_level, 'dB is as loud as quiet room')
    elif sound_level < 40:
        print(sound_level, 'dB is quieter than quiet room')

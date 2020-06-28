# Radio waves Less than 3 × 1e09
# Microwaves 3 × 1e09 to less than 3 × 10e12
# Infrared light 3 × 10e12 to less than 4.3 × 10e14
# Visible light 4.3 × 10e14 to less than 7.5 × 10e14
# Ultraviolet light 7.5 × 10e14 to less than 3 × 10e17
# X-rays 3 × 10e17 to less than 3 × 10e19
# Gamma rays 3 × 10e19 or more

while True:
    freq = float(input('Input frequency in Hz: '))

    if freq < 0.0:
        print('Frequency cannot be negative')
    else:
        if freq < 3e9:
            radiation = 'radio waves'
        elif 3e9 <= freq < 3e12:
            radiation = 'microwaves'
        elif 3e12 <= freq < 4.3e14:
            radiation = 'infrared light'
        elif 4.3e12 <= freq < 7.5e14:
            radiation = 'visible light'
        elif 7.5e14 <= freq < 3e17:
            radiation = 'ultraviolet light'
        elif 3e17 <= freq < 3e19:
            radiation = 'x-rays'
        else:
            radiation = 'gamma rays'

        print('Radiation with the frequency of %.0e Hz is called %s' % (freq, radiation))

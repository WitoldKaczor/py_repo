# Violet 380 to less than 450
# Blue 450 to less than 495
# Green 495 to less than 570
# Yellow 570 to less than 590
# Orange 590 to less than 620
# Red 620 to 750

while True:
    wavelength = float(input('Input a wavelength in nm: '))

    if wavelength < 380 or wavelength > 750:
        print('Wavelength outside of the visible spectrum (380..750)nm')
    else:
        if 380 <= wavelength < 450:
            color = 'Violet'
        elif 450 <= wavelength < 495:
            color = 'Blue'
        elif 495 <= wavelength < 570:
            color = 'Green'
        elif 570 <= wavelength < 590:
            color = 'Yellow'
        elif 590 <= wavelength < 620:
            color = 'Orange'
        else:
            color = 'Red'

        print('The wavelength of %.0f nm is equivalent to the color %s' % (wavelength, color))

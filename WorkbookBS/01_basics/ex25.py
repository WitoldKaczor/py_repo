sec_num = int(input('number of seconds: '))
print(sec_num, 'seconds in form DD:HH:MM:SS')

days = sec_num // 86400
if days != 0:
    sec_num %= days * 86400

hours = sec_num // 3600
if hours != 0:
    sec_num %= hours * 3600

minutes = sec_num // 60
if minutes != 0:
    sec_num %= minutes * 60

seconds = sec_num

print('{:02d}'.format(days), ':',
      '{:02d}'.format(hours), ':',
      '{:02d}'.format(minutes), ':',
      '{:02d}'.format(seconds), sep='')

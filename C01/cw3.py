from datetime import datetime


class Plant(object):
    type = 'tree'


dt = datetime(2020, 10, 26, 12, 15)

print('{:10.5}'.format('xylophone'))
print('{:+d}'.format(42))
print('{:4d}'.format(42))
print('{first} {last}'.format(first='Hodor', last='Hodor!'))
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))


# -*- coding: utf-8 -*-
from datetime import date
from datetime import timedelta

year = input('Ingrese el año:')
month = input('ingrese el mes:')
day = input('ingrese el dia:')

birth_date = date(year, month, day)
current_birth_date = birth_date.replace(year=2016)

dt = date.today() - current_birth_date

if dt.days == 0:
	print 'Felicidades hoy es tu cumpleaños'
elif dt.days < 0:
	print 'Faltan {} dias para tu cumpleaños'.format(dt.days * -1)
else:
	print 'Pasaron {} dias desde tu cumpleaños'.format(dt.days)
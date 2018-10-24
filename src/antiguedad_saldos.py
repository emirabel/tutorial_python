# -*- coding: utf-8 -*-
from datetime import timedelta
from datetime import date
concentrado = {}
rangos = ('por vencer', '01_30', '31_60', '61_90', '> 90')
while True:
	folio = raw_input('Ingrese folio:')
	amount = input('Ingrese Importe:')
	year = input('Ingrese año[yyyy]:')
	month = input('Ingrese mes[mm]:')
	day = input('Ingrese dia[dd]:')
	mydate = date(year, month, day)
	delta = date.today() - mydate
	
	rango = 'por vencer'
	if delta.days > 0 and delta.days < 31:
		rango = '01_30'
	elif delta.days > 30 and delta.days < 61:
		rango = '31_60'
	elif delta.days > 60 and delta.days < 91:
		rango = '61_90'
	else:
		rango = '> 90'


	if concentrado.has_key(rango) == False:
		item = {'contador':1, 'total':amount}
		concentrado[rango] = item
	else:
		item = concentrado[rango]
		item['contador'] += 1
		item['total'] += amount

	if raw_input('¿Deseas continuar [S/N]?') in 'Nn':
		break;
	print '=' * 40

totales = []
contadores = []
for r in rangos:
	print r
	if concentrado.has_key(r):
		item = concentrado[r]
		totales.append(item['total'])
		contadores.append(item['contador'])
	else:
		totales.append(0)
		contadores.append(0)
print totales
print '\tX Vencer\t\t1-30\t\t31-60\t\t61-90\t\t>90'
print '$\t%s\t\t%s\t\t%s\t\t%s\t\t%s' % tuple(totales)
print '#\t%s\t\t%s\t\t%s\t\t%s\t\t%s' % tuple(contadores)




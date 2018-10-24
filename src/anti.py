# -*- coding: utf-8 -*-
from datetime import date
from datetime import timedelta

concentrado_importe = {'por_vencer':0, '01_30':0,'31_60':0,'61_90':0,'>90':0}
concentrado_facturas = {'por_vencer':0, '01_30':0,'31_60':0,'61_90':0,'>90':0}
n = input('Ingrese el Numero de facturas:')
while n > 0:
	n -= 1

	folio = input('Ingrese el folio: ' )
	importe = input('Ingrese el importe ')
	anio = input('Ingrese el año vto.[yyyy]: ')
	mes = input('Ingrese el mes vto[mm]: ')
	dia = input('Ingrese el dia vto.[dd]: ')

	fecha_vencimiento = date(anio, mes, dia)
	dias = (date.today() - fecha_vencimiento).days
	print 'dias de vencimiento ', dias 
	if dias >= 1 and dias <= 30:
		rango = '01_30'
	elif dias > 30 and dias <= 60:
		rango = '31_60'
	elif dias > 60 and dias <= 90:
		rango = '61_90'
	elif dias > 90:
		rango = '>90'
	else:
		rango = 'por_vencer'
	concentrado_importe[rango] += importe
	concentrado_facturas[rango] += 1
print
print '\tPor vencer\t1-30\t31-60\t61-90\t>90'
print 'Numero\t{}\t{}\t{}\t{}\t{}'.format(concentrado_facturas['por_vencer'], concentrado_facturas['01_30'], concentrado_facturas['31_60'], concentrado_facturas['61_90'], concentrado_facturas['>90'])
print 'Total\t{}\t{}\t{}\t{}\t{}'.format(concentrado_importe['por_vencer'], concentrado_importe['01_30'], concentrado_importe['31_60'], concentrado_importe['61_90'], concentrado_importe['>90'])











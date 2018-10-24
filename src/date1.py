# -*- coding: utf-8 -*-#
from datetime import date
from datetime import timedelta

print "Calcular fecha de vencimiento."
delta = timedelta(30, 0, 0)
fecha_vencimiento = date.today() + delta
print 'Fecha de factura: {}\nDías de crédito: {}  \nFecha de fecha_vencimiento: {}'.format(date.today(), delta.days, fecha_vencimiento)
print
print "Calcular periodo de los ultimos 3 meses"
delta = timedelta(90, 0, 0)
fecha_final = date.today()
fecha_inicial = fecha_final - delta
print 'Fecha inicial: {}\nFecha Final: {}'.format(fecha_inicial, fecha_final)

print
print "Mismo dia de la fecha inicial"
fecha_final = fecha_final.replace(day=fecha_inicial.day)
print 'Nueva fecha final:', fecha_final
print 'Número de día en la semana: {}  (0 = Lunes 6 = Domingo) '.format(fecha_final.weekday())
print 'Formato Personalizado(yyyy-mm-dd): {}'.format(fecha_final.strftime("%Y.%m.%d"))
print 'Formato ISO(mm-dd-yyyy): {}'.format(fecha_final.strftime("%Y.%m.%d"))

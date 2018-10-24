# -*- coding: utf-8 -*-
miarchivo = file('archivo.txt', 'r')
contenido = miarchivo.read()
print "Archivo completo\n\n", contenido
print
print 'posición despues de leer el archivo: ', miarchivo.tell()
miarchivo.seek(0)
print 'posición al mover el puntero al inicio', miarchivo.tell()
for linea in miarchivo.readlines():
	columnas =  linea.split('|')
	if columnas[5] == 'F':
		columnas[5] = 'Femanino'
	else:
		columnas[5] = 'Masculino'
	print '{}\t{}\t{}\t{}\t\t\t{}\t\t{}\t'.format(columnas[0], columnas[1], columnas[2], columnas[3], columnas[4], columnas[5])


miarchivo.close()
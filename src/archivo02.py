# -*- coding: utf-8 -*-
import os
nombre_archivo = 'archivo.txt'
if os.path.isfile(nombre_archivo) == False:
	print "Archivo no valido"
	exit()

miarchivo = file(nombre_archivo, 'a')
while True:
	numero_control = raw_input('Ingrese numero de control: ')
	if numero_control == 'salir':
		break
	nombre = raw_input('Ingrese numero de nombre: ')
	apellido_paterno = raw_input('Ingrese numero de apellido paterno: ')
	apellido_materno = raw_input('Ingrese numero de apellido materno: ')
	promedio = input('Ingrese el promedio: ')
	sexo = raw_input('Ingrese el sexo[M/F]: ')
	miarchivo.seek(0, os.SEEK_END)
	miarchivo.write('{}|{}|{}|{}|{}|{}\n'.format(numero_control.zfill(8), nombre, apellido_paterno, apellido_paterno, promedio, sexo))
miarchivo.close()
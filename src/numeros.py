# -*- coding: utf-8 -*-
class Numeros():
	def __init__(self):
		self.lista_numeros = []
	def agregar(self, n):
   		self.lista_numeros.append(n) 

	def mayor(self):
		primera_vez = True
		mayor = 0
		for n in self.lista_numeros:
			if primera_vez:
				mayor = n
				primera_vez = False
			elif n > mayor:
				mayor = n
		return mayor

	def promedio(self):
		if len(self.lista_numeros) == 0:
			return 0.0
		sumatoria = 0
		for n in self.lista_numeros:
			sumatoria += float(n)
		return sumatoria / len(self.lista_numeros)

misnumeros = Numeros()
misnumeros.agregar(5)
misnumeros.agregar(1)
misnumeros.agregar(4)
misnumeros.agregar(-1)
print 'El mayor es {}'.format(misnumeros.mayor())
print 'El promedio {}'.format(misnumeros.promedio())















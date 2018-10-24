# -*- coding: utf-8 -*-#
class Dog():  # Definición de clase
	__name = ''  # <--- propiedad nombre
	
	def bark(self):  # <-- metodo para ladrar.
		print "{}, guau... guau... ".format(self.name)
		print

	@property	
	def name(self):
		return self.name

	@name.setter
	def name(self, name):
		self.name = name
	
''' Instancia de clase perro Doqui '''
perro1 = Dog()
perro1.name = ''
print perro1.name

''' Instancia de clase perro Firulaes '''
perro2 = Dog()
perro2.name = 'Firulaes'

''' Perros ladran '''
perro2.bark();
perro1.bark();
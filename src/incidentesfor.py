lista = [0 , 0, 0, 0]
lista2 = lista[:]
for n in lista2:
	numero = input('ingresa el numero:')
	if numero < 0:
		break
	lista.append(numero)
print lista

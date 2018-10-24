# -*- encoding: utf-8 -*-
apertura = {')':'(', ']':'[','}':'{'}
stack = []

def evalua(expresion):
	error = False
	for caracter in expresion:
		if caracter in '([{':
			stack.append(caracter)
		elif caracter in ')]}':
			caracter_apertura = apertura[caracter]
			if not stack:
				error = True
				break
			caracter_pila = stack.pop()
			if caracter_apertura != caracter_pila:
				error = True
				break
	return error

expresion = raw_input('Ingrese la expresión:')
if not expresion:
    print 'Error expresión no valida'

if evalua(expresion):
	print 'Expresión no balanceada ', expresion
else:
	print 'Expresión Valida...', expresion
print stack

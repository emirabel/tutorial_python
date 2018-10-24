# -*- coding: utf-8 -*-
def listas_iguales(l1, l2):
	if len(l1) != len(l2):
		return False
	for i in range(len(l1)):
		if l1[i] != l2[i]:
			return False
	return True

l1 = [1, 2, 3]
l2 = [1, 2]
print 'Comparando l1 con l2: ', listas_iguales(l1, l2)

l3 = [1, 2, 3]
l4 = [1, 2, 3]
print 'Comparando l3 con l4: ', listas_iguales(l3, l4)

l5 = [3, 2, 1]
print 'Comparando l4 con l5: ', listas_iguales(l4, l5)
# -*- coding: utf-8 -*-

def es_primo(n):
	if n == 1:
		return False
	for i in range(2, n-1):
		if n % i is 0:
			return False
	return True

for i in range(0, 100):
	primo = es_primo(i)
	if primo:
		print i, "/t", primo



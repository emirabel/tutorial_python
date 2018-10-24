# -*- encoding: utf-8 -*-

def list_equal(l1, l2):
	if len(l1) != len(l2):
		return False
	for i in range(len(l1)-1):
		if l1[i] != l2[i]:
			return False
	return True

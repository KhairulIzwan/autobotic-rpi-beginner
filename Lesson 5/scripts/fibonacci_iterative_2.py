#!/usr/bin/env python

def fib(n):
	a, b, = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a

for i in range (0, 10):
	print(fib(i))

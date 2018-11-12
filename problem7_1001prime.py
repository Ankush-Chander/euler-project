'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+'/util')


import numbers_lib

if len(sys.argv) !=2:
	print("Usage: python "+sys.argv[0]+" number")
else:
	high = int(sys.argv[1])
	current = -1
	for i in numbers_lib.generate_primes():
		current = current + 1
		if current == high:
			# print(current)
			print(i)
			break
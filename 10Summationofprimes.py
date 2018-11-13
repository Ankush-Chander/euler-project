'''
'''

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/util')

import numbers_lib

if len(sys.argv) != 2:
	print("Usage: python " + sys.argv[0] + " number")
else:
	number = int(sys.argv[1])
	# print(number)

	prime_sum = 0
	for i in numbers_lib.get_primes_less_than_n(number):
		prime_sum = prime_sum + i
	print(prime_sum)
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

# complexity: n^2 
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+'/util')


import numbers_lib


if len(sys.argv) !=2:
	print("Usage: python " + sys.argv[0] + " number")
else:
	max = int(sys.argv[1])			

	result = 1
	product = 1
	for i in numbers_lib.get_primes(max/2 +1):		
		if max % i == 0:
			result = i			
			product = product*result
			if product == max: #micro management
				break
	print(result)
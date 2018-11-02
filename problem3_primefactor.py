# language: python
# complexity: n^2 
import sys

sys.path.append('/home/ankush/projects/euler/util')

print(sys.path)
import numbers_lib


if len(sys.argv) !=2:
	print("Usage: problem3_primefactor.py number")
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
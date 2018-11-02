import sys

sys.path.append('/home/ankush/projects/euler/util')

import numbers_lib

if len(sys.argv) !=2:
	print("Usage: python "+sys.argv[0]+" number")
else:
	high = int(sys.argv[1])
	numbers = range(1,high)
	print(numbers_lib.calculateLcm(numbers))
# 	prime_array = [0]* (high + 1)
#
#
# 	for j in range(1,high+1):
# 		factors = numbers_lib.factorize_number(j)
# 		freq = Counter(factors)
# 		for item in freq:
# 			prime_array[item] = max(freq[item],prime_array[item])
#
# 	# print(prime_array)
#
# lcm = 1
# for i in range(0,high+1):
# 	lcm = lcm * i**(prime_array[i])
#
# print(lcm)
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+'/util')

import numbers_lib

if len(sys.argv) !=2:
	print("Usage: python " + sys.argv[0] + " max_limit")
else:
	max = int(sys.argv[1])

sum = 0
for i in range(3,max):
	if numbers_lib.is_multiple(i,3) or numbers_lib.is_multiple(i,5):
		sum = sum + i
print(sum)		

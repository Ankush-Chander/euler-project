'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
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
	numbers = range(1,high)
	print(numbers_lib.calculateLcm(numbers))
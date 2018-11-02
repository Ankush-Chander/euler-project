'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3 digit numbers.
'''
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+'/util')


import numbers_lib


largest_pallindrome= 0
if len(sys.argv) !=2:
	print("Usage: python "+sys.argv[0]+" digits")
else:
	digits = int(sys.argv[1])
	low = 10**(digits-1)
	high = (10**digits)-1
	# cheap brute force solution doesnt work for more than 3 digits (improve later)
	for i in reversed(range(low,high)):
		for j in reversed(range(low,high)):
			if numbers_lib.isNumberpallindrome(i*j):
				largest_pallindrome= max(i*j,largest_pallindrome)

	print(largest_pallindrome)	

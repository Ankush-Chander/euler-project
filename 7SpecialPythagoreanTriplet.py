'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import sys
import os


if len(sys.argv) != 2:
	print("Usage: python " + sys.argv[0] + " number")
else:
	number = int(sys.argv[1])
	# print(number)
	for i in range(1,number):
		for j in range(1,number-i):
			k = number-(i+j)
			if i**2 + j**2 == k**2:
				print(i,j,k)
				print(i*j*k)
				break
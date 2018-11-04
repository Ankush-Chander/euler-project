'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import sys

if len(sys.argv) !=2:
	print("Usage: python "+sys.argv[0]+" number")
else:
	high = int(sys.argv[1])

	squareOfSum = sum([i for i in range(1,high+1)])**2
	sumOfSquares = sum([i**2 for i in range(1,high+1)])

	print(squareOfSum - sumOfSquares)
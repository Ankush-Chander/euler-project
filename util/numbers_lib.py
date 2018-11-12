'''Number based functions'''
from collections import Counter
import math as math

'''check if a number is prime
	time complexity: n
'''

def is_multiple(divisor, dividend):
	return (divisor%dividend == 0)


def is_prime(number):
	for i in range(2,number/2+1):
		if is_multiple(number, i):
			return False
	return True


'''get prime numbers less than a given number
   time complexity: n^2 	
'''
def get_primes(number):
	i =1
	while i < number:
		if is_prime(i):
			yield i
		i = i +1

'''
get prime using sieve of eratosthenes
'''
def get_primes_less_than_n(n): # works fine for smaller values of n
	x = [i for i in range(2,n+1)]
	max_divisor = round(math.sqrt(n))
	while len(x)>0:
		current_prime = x[0]
		yield current_prime
		# eliminate all the multiples of prime under scanner
		if x[0] < max_divisor:
			y = [j for j in x if j%current_prime!=0 and j > current_prime]
		else:
			y = x[1:]
		x = y


def factorize_number(number):
	factors = []
	if is_prime(number):
		factors.append(number)
		return factors
	i=2
	while number != 1:
		if is_prime(number):
			factors.append(number)
			break	
		elif number %i ==0:
			factors.append(i)
			number = number/i
		else:
			i = i+1

	return factors

def calculateLcm(number_list):
	high = max(number_list)
	prime_array = [0] * (high + 1)

	for j in number_list:
		factors = factorize_number(j)
		freq = Counter(factors)
		for item in freq:
			prime_array[item] = max(freq[item], prime_array[item])

	lcm = 1
	for i in range(0, high + 1):
		lcm = lcm * i ** (prime_array[i])

	return(lcm)


def fibGenerator(max_number):
	i=0
	j=1
	while j < max_number:
		temp = i
		i=j
		j=temp+j
		yield (j)

def reverse_number(number):
	number = str(number)
	return int(number[::-1])

def isNumberpallindrome(number):
	return number == reverse_number(number)

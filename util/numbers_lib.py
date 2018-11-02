'''Number based functions'''
from collections import Counter

'''check if a number is prime
	time complexity: n
'''
def is_prime(number):
	
	for i in range(2,number/2+1):
		if number % i ==0:
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

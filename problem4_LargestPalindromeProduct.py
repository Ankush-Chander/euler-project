import sys

def reverse_number(number):
	number = str(number)
	return int(number[::-1]) 

def isNumberpallindrome(number):
	return number == reverse_number(number)  


largest_pallindrome= 0
if len(sys.argv) !=2:
	print("Usage: python "+sys.argv[0]+" digits")
else:
	digits = int(sys.argv[1])
	low = 10**(digits-1)
	high = (10**digits)-1
	# cheap solution doesnt work for more than 3 digits (can do better)
	for i in reversed(range(low,high)):
		for j in reversed(range(low,high)):
			if isNumberpallindrome(i*j):			
				largest_pallindrome= max(i*j,largest_pallindrome)

	print(largest_pallindrome)	

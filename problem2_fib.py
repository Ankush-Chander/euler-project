import sys

def fib(previous, next_v):	
	return((next_v, previous + next_v ))


if len(sys.argv) !=2:
	print("Usage: problem2_fib.py max_limit")
else:
	max = int(sys.argv[1])

	previous_value = 1
	current_value = 1
	
	total = 0

	while current_value < max:		
		(previous_value, current_value) = fib(previous_value, current_value)

		if current_value%2 ==0:
			total = total+ current_value 

print(total)
function is_multiple(divisor, dividend):
	return (divisor%dividend == 0) 

sum = 0
for i in range(3,1000):
	if is_multiple(i,3) or is_multiple(i,5):
		print(i)
		sum = sum + i
print(sum)		

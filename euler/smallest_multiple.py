def isPrime(n):
	for x in range(2, int(n**0.5+1)):
		if n % x == 0:
			return False
	return True

primeDivisors = [x for x in range(1, 21) if isPrime(x)]
print primeDivisors
def sumMult(multiples):
	total = 1
	for x in multiples:
		total = total*x
	return total*24
	
print sumMult(primeDivisors)
import math

numlist = []
def isprime(n):
	for number in range(2, n/2+1):
		if n % number == 0:
			return False
	return True

def factorlist(n):
	for number in range(2, int(math.sqrt(n))):
		if n % number == 0:
			numlist.append(number)
factorlist(600851475143)
primelist = []
for n in numlist:
	if isprime(n):
		primelist.append(n)
		
print primelist
print 600851475143/6857.0
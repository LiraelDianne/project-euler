def isprime(num):
	for i in range(2, int(num**0.5+1)):
		if num % i == 0:
			return False
	return True

def primesbelow(n):
	primes = []
	for i in range(2, n):
		if isprime(i):
			primes.append(i)
	return primes
primes = primesbelow(2000000)
total = 0
for num in primes:
	total += num
print total
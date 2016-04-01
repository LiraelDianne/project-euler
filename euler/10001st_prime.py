def isPrime(n):
	for x in range(2, int(n**0.5+1)):
		if n % x == 0:
			return False
	return True

primes = []
i = 2
while len(primes) < 10001:
	if isPrime(i):
		primes.append(i)
	i += 1

print primes[10000]

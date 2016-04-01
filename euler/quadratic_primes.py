def isprime(n):
	for number in range(2, n/2+1):
		if n % number == 0:
			return False
	return True

def how_many(a, b):
	n = 0
	while isprime(abs(n**2+a*n+b)):
		n += 1
	return n

most = 1
amost = 0
bmost = 0

for a in range(999, -1000, -2):
	for b in range(-999, 1000, 2):
		primes = how_many(a, b)
		if primes > most:
			most = primes
			amost = a
			bmost = b
print most, amost, bmost
print amost*bmost
def divisors(n):
	divisors = 1
	for i in range(1, int(n/2+1)):
		if n % i == 0:
			divisors += 1
	return divisors
	
trinum = 1
inc = 1
highest = 0
divis = divisors(trinum)
while divis < 500:
	inc += 1
	trinum += inc
	divis = divisors(trinum)
	if divis > highest:
		highest = divis
		print inc, trinum, divis
	if inc % 1000 == 0:
		print inc, trinum
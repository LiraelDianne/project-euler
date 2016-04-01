def collatz(n, cursions):
	recursion = cursions + 1
	if n == 1:
		return recursion
	if n % 2 == 0:
		return collatz(n/2, recursion)
	else:
		return collatz(3*n+1, recursion)
	
longest = 0
starting = 0
for i in range(1, 1000000):
	chain = collatz(i, 0)
	if chain > longest:
		longest = chain
		starting = i
		print starting, longest

print starting, "produces chain of", longest
	
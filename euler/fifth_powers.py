total = 0
for n in range(2, 1000000):
	digits = [int(digit)**5 for digit in str(n)]
	if sum(digits) == n:
		total += n
print total
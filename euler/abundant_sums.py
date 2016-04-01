def divisors(n):
	divisors = []
	for i in range(1, int(n/2+1)):
		if n % i == 0:
			divisors.append(i)
	return divisors
	
abundant = []
for n in range(1, 28124):
	if sum(divisors(n)) > n:
		abundant.append(n)
print "abundants calculated"
abundsums = []
def abundsum(n):
	for i in abundant:
		if i > n:
			break
		for j in abundant:
			if j > n:
				break
			if i+j == n:
				return True
	return False

twothousand = 0
for n in range(1, 28124):
	if twothousand == 3000:
		print n
		break
	if abundsum(n):
		abundsums.append(n)
		if len(abundsums) > 2:
			if abundsums[-1] == abundsums[-2]+1:
				twothousand += 1
			else:
				twothousand = 0

notabundsum = []
for i in range(1, abundsums[-1]):
	if i not in abundsums:
		notabundsum.append(i)
		
print sum(notabundsum)
		
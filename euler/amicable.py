def divisors(n):
	divisors = []
	for i in range(1, int(n/2+1)):
		if n % i == 0:
			divisors.append(i)
	return divisors
	
def amic(n):
	divis = divisors(n)
	amicsum = sum(divis)
	if amicsum != n and sum(divisors(amicsum)) == n:
		return True
	else:
		return False
amiclist = []
for n in range(1, 10000):
	if amic(n):
		amiclist.append(n)
		
print amiclist
print sum(amiclist)

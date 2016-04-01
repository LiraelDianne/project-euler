from decimal import *
getcontext().prec = 2000
fractions = [Decimal(1)/Decimal(x) for x in range(983, 984) if len(str(Decimal(1)/Decimal(x))) > 10]

def repeat_length(num):
	if len(num) <= 3:
		print 'no repeat found'
		return 'no repeat found'
	for depth in range(3, len(num)):
		if num[:depth] == num[depth:depth+depth]:
			return depth
	else:
	    return repeat_length(num[1:])
	    


longest = 1
for fraction in fractions:
	string = str(fraction)[2:-1]
	repeat = repeat_length(string)
	if repeat == 'no repeat found':
		print fraction
	elif repeat > longest:
		longest = repeat
print longest

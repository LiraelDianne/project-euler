product = 1
for n in range(100, 0, -1):
	product = product*n
	
stri = str(product)
total = 0
for num in stri:
	total += int(num)
print total
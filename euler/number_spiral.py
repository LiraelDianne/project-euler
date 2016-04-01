diagonals = [1]
skip = 1
pick = 0
cycle = 0
for n in range(2, 1001*1001+1):
	if pick == skip:
		cycle += 1
		pick = 0
		diagonals.append(n)
	else:
		pick += 1
	if cycle == 4:
		skip += 2
		cycle = 0
	
print sum(diagonals)
	
def pascal(depth):
	row = [0, 1, 0]
	for n in range(1, depth):
		row.append(0) 
		newrow = [0]
		for num in range(1, len(row)):
			newrow.append(row[num]+row[num-1])
		row = newrow
	return row

lattice = pascal(41)
lattice.sort()
print lattice[len(lattice)-1]
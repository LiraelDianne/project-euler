f = open("grid.txt", "r")
grid = []
for line in f:
	row = line.split()
	grid.append(row)
f.close()
for line in range(len(grid)):
	for col in range(len(grid)):
		grid[line][col] = int(grid[line][col])	
def horizontal(grid):
	biggest = 0
	for line in grid:
		for col in range(len(line)-3):
			product = line[col]*line[col+1]*line[col+2]*line[col+3]
			if product > biggest:
				biggest = product
	return biggest	
			
def vertical(grid):
	biggest = 0
	for row in range(len(grid)-3):
		for col in range(len(grid[row])):
			product = grid[row][col]*grid[row+1][col]*grid[row+2][col]*grid[row+3][col]
			if product > biggest:
				biggest = product
	return biggest

def diagonalDown(grid):
	biggest = 0
	for row in range(len(grid)-3):
		for col in range(len(grid[row])-3):
			product = grid[row][col]*grid[row+1][col+1]*grid[row+2][col+2]*grid[row+3][col+3]
			if product > biggest:
				biggest = product
	return biggest
	
def diagonalUp(grid):
	biggest = 0
	for row in range(len(grid)-3):
		for col in range(3, len(grid[row])):
			product = grid[row][col]*grid[row+1][col-1]*grid[row+2][col-2]*grid[row+3][col-3]
			if product > biggest:
				biggest = product
	return biggest

finals = []
finals.append(horizontal(grid))
finals.append(vertical(grid))
finals.append(diagonalDown(grid))
finals.append(diagonalUp(grid))
print finals
finals.sort()

print finals[len(finals)-1]

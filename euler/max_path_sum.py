f = open("number_triangle.txt", "r")
tri = []
for line in f:
	row = line.split()
	newrow = []
	for num in row:
		newrow.append(int(num))
	tri.append(newrow)
f.close()
print tri

def splitter(coords, sum):
	if coords[1] == len(tri[coords[0]])-1:
	    return sum
	sum1 = sum + tri[coords[0]][coords[1]]
	sum2 = sum + tri[coords[0]][coords[1]+1]
	if coords[0] == len(tri)-1:
		if sum1 > sum2:
			return sum1
		else:
			return sum2
	else:
		path1 = (coords[0]+1, coords[1])
		path2 = (coords[0]+1, coords[1]+1)
		finalsum1 = splitter(path1, sum1)
		finalsum2 = splitter(path2, sum2)
		if finalsum1 > finalsum2:
			return finalsum1
		else:
			return finalsum2

print splitter((1, 0), tri[0][0])

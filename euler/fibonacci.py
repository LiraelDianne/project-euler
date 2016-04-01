def fibonacci():
	index = 0
	a = 0
	b = 1
	while len(str(b)) < 1000:
		a, b = b, a+b
		index += 1
	print a, b, index

fibonacci()
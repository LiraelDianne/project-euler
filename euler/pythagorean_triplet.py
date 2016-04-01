squares = [x**2 for x in range(1, 500)]
abcs = []
for square in squares:
	for square2 in squares:
		if square2 > square and (square + square2) in squares:
			abcs.append((square, square2, (square + square2)))

for tuple in abcs:
	a = tuple[0]**0.5
	b = tuple[1]**0.5
	c = tuple[2]**0.5
	if a + b + c == 1000:
		print a, b, c
		print a * b * c
		
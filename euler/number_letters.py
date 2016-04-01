numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
later = ["teen", "ty", "hundred"]
tens = ["twenty", "thirty", "forty", "fifty"]
for x in range(4):
	if x == 2:
		numbers.append(numbers[6+x][:-1]+"teen")
		tens.append(numbers[6+x][:-1]+"ty")
	else:
		numbers.append(numbers[6+x]+"teen")
		tens.append(numbers[6+x]+"ty")

for ten in range(8):
	for one in range(10):
		numbers.append(tens[ten]+numbers[one])

tohundred = numbers[:]
for hundred in range(9):
	for num in tohundred:
		if num == "":
			numbers.append(numbers[hundred+1]+"hundred"+num)
		else:
			numbers.append(numbers[hundred+1]+"hundredand"+num)
			
numbers.append("onethousand")
total = 0
for num in numbers:
	total += len(num)
print total
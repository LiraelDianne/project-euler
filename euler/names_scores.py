import string

f = open("names.txt", "r")
names = f.readlines()
f.close()
names[0] = names[0].replace('"', '')
names = names[0].split(",")

names.sort()
ab = string.uppercase
total = 0
for n, name in enumerate(names):
	score = 0
	for char in name: 
		score += 1+ab.index(char)
	score = score * (n+1)
	total += score
print total
f = open("50digitnumbers.txt", "r")
fifties = []
for line in f:
	fifties.append(int(line[:50]))
f.close()
total = 0
for num in fifties:
	total += num
print str(total)[:10] 
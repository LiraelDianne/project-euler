unique = []
for base in range(2, 101):
    for power in range(2, 101):
	    if base**power not in unique:
		    unique.append(base**power)
unique.sort()
print len(unique)
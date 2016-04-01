permute = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 1
stop = 0
def iterate():
	global permute, count
	for digit in range(len(permute)-2, -1, -1):
		if permute[digit+1] > permute[digit]:
			count += 1
			# digit is now the location of the farthest right digit where the digit to the right is higher
			swap = 10
			tail = [permute[digit]]
			for following in permute[digit+1:]:
				tail.append(following)
				if swap > following > permute[digit]:
					swap = following
			if swap in tail:
				tail.remove(swap)
			newpermute = permute[:digit]
			newpermute.append(swap)
			tail.sort()
			if tail != []:
				newpermute.extend(tail)
			permute = newpermute
			break
while count < 1000000:
	previouscount = count
	iterate()
	if count % 100000 == 0:
		print " count", count, permute
	if previouscount == count:
		stop += 1
	else: stop = 0
	if stop > 20:
		print "froze at", count, permute
		break
print "count", count, permute
		

		
		

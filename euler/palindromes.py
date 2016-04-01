multiples = [x for x in range(1000, 100, -1)]
pali = []
def pals(multiples):
	for n in multiples:
		for m in multiples:
			mult = str(n*m)
			if mult == mult[::-1]:
				pali.append(n*m)
pals(multiples)
pali.sort()
print pali[len(pali)-1]
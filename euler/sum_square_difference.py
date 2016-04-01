hundred = [x for x in range(1, 101)]
def sumofsquares(nums):
	total = 0
	for num in nums:
		total += num**2
	return total

def squareofsums(nums):
	total = 0
	for num in nums:
		total += num
	return total**2

print squareofsums(hundred) - sumofsquares(hundred)
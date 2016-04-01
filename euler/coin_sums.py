def branch(total, coins):
	count = 1
	if total > 0:
		for coin in coins:
			if total >= coin:
				count += branch(total-coin, coins[:coins.index(coin)+1])
	return count
	
print branch(200, [2, 5, 10, 20, 50, 100, 200])


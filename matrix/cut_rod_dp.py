# 		0	1	2	3	4	5

# 	0	0	0	0	0	0	0	
		
# (2) 1	0	2	4	6	8	10

# (5) 2	0	2	5	7	10	12

# (7) 3	0	2	5	7	10	12

# (8) 4	0	2	5	7	10	12

def cutRod(price_array, dp):
	for row in range(1, len(price_array) + 1):
		for col in range(1, len(price_array) + 2):
			if row == 1:
				dp[row][col] = (col) * price_array[0]
			if col == 1:
				dp[row][col] = price_array[0]
			if row > col:
				dp[row][col] = dp[row - 1][col]
			else:
				dp[row][col] = max(dp[row -1 ][col], dp[row][col - row] + price_array[row - 1]  )

	for row in dp:
		print(row)

if __name__ == "__main__":
	price_array = [2, 5, 7, 8]
	# price_array = [3, 5, 8, 9, 10, 17, 17, 20]

	dp = [[0 for col in range(0, len(price_array ) + 2)] for row in range(0,len(price_array) + 1)]
	print(dp)
	cutRod(price_array, dp)



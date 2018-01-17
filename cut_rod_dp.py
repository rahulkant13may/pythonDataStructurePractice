# 		0	1	2	3	4	5

# 	0	0	0	0	0	0	0	
		
# (2) 1	0	2	4	6	8	10

# (5) 2	0	2	5	7	10	12

# (7) 3	0	2	5	7	10	12

# (8) 4	0	2	5	7	10	12

# Ques: Given a length of rod and price of different pieces of rod , then how you will cut the rod to maximize the profit

def cutRod(price_array, length, dp):
	for row in range(0, len(price_array) + 1):
		for col in range(length + 1):
			if row == 1:
				dp[row][col] = (col) * price_array[0]
			elif col == 1 and row > 0:
				dp[row][col] = price_array[0]
			elif row > col:
				dp[row][col] = dp[row - 1][col]
			elif row > 1 and col > 1 and row <=  col:
				dp[row][col] = max(dp[row -1 ][col], dp[row][col - row] + price_array[row - 1]  )

	for row in dp:
		print(row)

if __name__ == "__main__":
	price_array = [2, 5, 7, 8]
	length = 5

	dp = [[0 for col in range(length + 1)] for row in range(0,len(price_array) + 1)]
	cutRod(price_array, length, dp)







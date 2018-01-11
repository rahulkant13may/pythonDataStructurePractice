def isSubsetSum(st, n, sm):
	dp = [[0 for col in range(sm + 1)] for row in range(n)]
	for row in range(n):
		for col in range(sm + 1):
			if col == 0 or st[row] == col:
				dp[row][col] = 1

			elif row == 0  and col == st[row]:
				dp[row][col] = 1

			elif st[row] > col:
				dp[row][col] = dp[row - 1][col]

			elif st[row] < col:
				if dp[row - 1][col] == 1:
					dp[row][col] = 1

				else:
					dp[row][col] = dp[row - 1][col - st[row]]

	# print(dp)
	for x in dp:
		print(x)

	return dp[n -1][sm]


# Driver program to test above function
st = [2, 3, 7, 8, 10]
sm = 11
# st = [1, 2, 3]
# sm = 7
n = len(st)
if (isSubsetSum(st, n, sm) == True) :
    print("Found a subset with given sum")
else :
    print("No subset with given sum")


# 	0   1  2  3  4  5  6  7  8  9  10 11	

# 2	[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 3	[1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
# 7	[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
# 8	[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
# 10	[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]


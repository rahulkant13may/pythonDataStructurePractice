	# 	a b c d
	# b   0 1 1 1

	# d   0 1 1 2

	# c   0 1 2 2

	# e   0 1 2 2

def lcs(first, second):
	dp = [[0 for col in range(len(first))] for row in range(len(second))]

	for row in range(len(second)):
		for col in range(len(first)):
			# Filling first row of dp
			if row == 0:
				if second[0] == first[col]:
					dp[0][col] = 1
				elif second[0] != first[col] and col -1 >= 0:
					dp[0][col] = dp[0][col - 1]

			# Filling first column of dp
			if col == 0:
				if first[0] == second[row]:
					dp[row][0] = 1
				elif first[0] != second[row] and row - 1 >= 0:
					dp[row][0] = dp[row - 1][0]


			else:
				# if matches then add 1 to when last matches excluding current word
				if second[row] == first[col]:
					dp[row][col] = dp[row - 1][col - 1] + 1
				# if doest not matches then max of top and left from dp
				elif second[row] != first[col]:
					dp[row][col] = max(dp[row -1][col], dp[row][col - 1])

	# print(dp)
	for x in dp:
		print(x)

	return dp[len(second) - 1][len(first) - 1]

				


# Driver program to test the above function
# X = "AGGTAB"
# Y = "GXTXAYB"

X = "ABCD"
Y = "BDCE"
print("Length of LCS is ", lcs(X , Y))
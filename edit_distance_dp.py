
def editDistDP(str1, str2, m, n):
	dp = [[0 for col in range(m + 1)] for row in range(n + 1)]
	for row in range(n + 1):
		for col in range(m + 1):
			if row == 0:
				dp[row][col] = col
			elif col == 0:
				dp[row][col] = row
			elif str1[col - 1] == str2[row - 1]:
				dp[row][col] = dp[row - 1][col - 1]
			elif str1[col - 1] != str2[row - 1]:
				dp[row][col] = 1 + min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1])

	# for x in dp:
	# print(dp)
	for x in dp:
		print(x)




# Driver program
str1 = "abcdef"
str2 = "azced"
 
# print(editDistDP(str1, str2, len(str1), len(str2)))
# This code is contributed by Bhavya Jain

editDistDP(str1, str2, len(str1), len(str2))

#       a  b  c  d  e  f  
#   [0, 1, 2, 3, 4, 5, 6]
# a [1, 0, 1, 2, 3, 4, 5]
# z [2, 1, 1, 2, 3, 4, 5]
# c [3, 2, 2, 1, 2, 3, 4]
# e [4, 3, 3, 2, 2, 2, 3]
# d [5, 4, 4, 3, 2, 3, 3]
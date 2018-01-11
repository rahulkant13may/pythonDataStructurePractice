
def editDistDP(str1, str2, m, n):
	dp = [[0 for row in range(n + 2)] for col in range(m + 2)]
	for row in range(n + 1):
		for col in range(m + 1):
			if row = 0:
				dp[row][col] = col
			elif col = 0:
				dp[row][col] = row
			elif str1[]



# Driver program
str1 = "sunday"
str2 = "saturday"
 
print(editDistDP(str1, str2, len(str1), len(str2)))
# This code is contributed by Bhavya Jain
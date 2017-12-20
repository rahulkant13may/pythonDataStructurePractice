def findLongestPathFromCell(row, col, cost, dp):

	# Boundry condition 
	if (row >= len(cost[0]) or col >= len(cost[0]) or row < 0 or col < 0):
		return 0 

	# If this subproblem is already solved
	if (dp[row][col] != -1):
		return dp[row][col]

    # Since all numbers are unique and in range from 1 to n*n,
    # there is atmost one possible direction from any cell
	if (col + 1 < len(cost[0])) and (cost[row][col + 1] == cost[row][col] + 1):
		return 1 + findLongestPathFromCell(row, col + 1, cost, dp)

	if (col - 1 >= 0) and (cost[row][col - 1] == cost[row][col] + 1):
		return 1 + findLongestPathFromCell(row, col - 1, cost, dp)

	if (row + 1 < len(cost[0])) and (cost[row + 1][col] == cost[row][col] + 1):
		return 1 + findLongestPathFromCell(row + 1, col, cost, dp)

	if (row - 1 >= 0) and (cost[row - 1][col] == cost[row][col] + 1):
		return 1 + findLongestPathFromCell(row - 1, col, cost, dp)

	# If none of the adjacent fours is one greater
	else:
		dp[row][col] = 1
		return 1 


# Returns length of the longest path beginning with any cell
def LongestPath(cost):
	dp = [[-1]*len(cost[0]) for i in cost]
	result = 1
	for row in range(0, len(cost[0])):
		for col in range(0, len(cost[0])):
			dp[row][col] = findLongestPathFromCell(row, col, cost, dp)
			result = max(result, dp[row][col])
	# print(dp)
	print(result)


# Driver program to test above functions
if __name__ == "__main__":
    cost = [[1, 2, 9 ],
            [5, 3, 8 ],
            [4, 6, 7 ]]

    LongestPath(cost)
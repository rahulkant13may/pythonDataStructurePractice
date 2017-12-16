
def findLongestPathFromCell(row, col, cost, dp):
	print(dp, row, col)
	if (row > len(cost[0]) or col > len(cost[0]) or row < 0 or col < 0):
		return 0 

	if (dp[row][col] != -1):
		return dp[row][col]

	if (col + 1 < len(cost[0])) and (cost[row][col + 1] == cost[row][col] + 1):
		return 1 + findLongestPathFromCell(row, col + 1, cost, dp)

	if (col - 1 > 0) and (cost[row][col - 1] == cost[row][col] + 1):
		return 1 + findLongestPathFromCell(row, col - 1, cost, dp)

	if (row + 1 < len(cost[0])) and (cost[row + 1][col] == cost[row][col] + 1):
		return 1 + findLongestPathFromCell(row + 1, col, cost, dp)

	if (row - 1 > 0) and (cost[row - 1][col] == cost[row][col] + 1):
		return 1 + findLongestPathFromCell(row - 1, col, cost, dp)
	else:
		dp[row][col] = 1
		return 1 



def LongestPath(cost):
	dp = [[-1]*len(cost[0]) for i in cost]
	findLongestPathFromCell(2, 1, cost, dp)
	# for row in range(0, len(cost[0])):
	# 	for col in range(0, len(cost[0])):
	# 		dp[row][col] = findLongestPathFromCell(row, col, cost, dp)
	print("#######################")
	print(dp)
		


# Driver program to test above functions
if __name__ == "__main__":
    cost = [[1, 2, 9 ],
            [5, 3, 8 ],
            [4, 6, 7 ]]

    LongestPath(cost)
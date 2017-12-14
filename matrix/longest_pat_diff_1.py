

def LongestPath(cost):
	dp = [[0]*len(cost[0]) for i in cost]
	for row in range(0, len(cost[0])):
		for col in range(0, len(cost[0])):
			if dp[row][col] == 0:
				


# Driver program to test above functions
if __name__ == "__main__":
    cost = [[1, 2, 3, 4 ],
            [2, 2, 3, 4],
            [3, 2, 3, 4],
            [4, 5, 6, 7]]

    print(LongestPath(cost))
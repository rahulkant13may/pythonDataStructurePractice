def longestPath(cost):
	dp = [[0 for x in range(3)] for x in range(3)]
	for row in range(3):
		for col in range(3):
			if dp[row][col] == 0:
				print(row, col)
				dp_lp = [[0 for x in range(3)] for x in range(3)]
				result = 1
				for r in range(3):
					for c in range(3):
						if dp_lp[r][c] == 0:
							dp_lp[r][c] = 1
						#right
						if (c + 1 < 3) and (cost[r][c + 1] == cost[r][c] + 1) and (dp_lp[r][c + 1] < dp_lp[r][c] + 1):
							dp_lp[r][c + 1] = dp_lp[r][c] + 1
						#left
						if (c - 1 >= 0) and (cost[r][c - 1] == cost[r][c] + 1) and (dp_lp[r][c - 1] < dp_lp[r][c] + 1):
							dp_lp[r][c - 1] = dp_lp[r][c] + 1
						#down
						if (r + 1 < 3) and (cost[r + 1][c] == cost[r][c] + 1) and (dp_lp[r + 1][c] < dp_lp[r][c] + 1):
							dp_lp[r + 1][c] = dp_lp[r][c] + 1
						#up
						if (r - 1 >= 0) and (cost[r - 1][c] == cost[r][c] + 1) and (dp_lp[r - 1][c] < dp_lp[r][c] + 1):
							dp_lp[r - 1][c] = dp_lp[r][c] + 1

				print(dp_lp)
	# print(dp)





cost = [[1, 2, 9],
        [5, 3, 8],
        [4, 6, 7]]

longestPath(cost)
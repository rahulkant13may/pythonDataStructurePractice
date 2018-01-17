R = 3 
C = 3

def minCostPath(cost, rowDest, colDest):
	#initilaize all values with 0
	minCostMatrixTable = [[0 for x in range(R)] for x in range(C)]

	#initialize minCostMatrixTable[0][0] with cost[0][0] because it is initial position
	minCostMatrixTable[0][0] = cost[0][0]

	#initialize first column values
	for row in range(1, R):
		minCostMatrixTable[row][0] = minCostMatrixTable[row - 1][0] + cost[row][0]

	#initialize first row values
	for col in range(1, C):
		minCostMatrixTable[0][col] = minCostMatrixTable[0][col - 1] + cost[0][col]

	for row in range(1, R):
		for col in range(1, C):
			minCostMatrixTable[row][col] = min(minCostMatrixTable[row -1][col], minCostMatrixTable[row][col -1], minCostMatrixTable[row -1][col -1]) + cost[row][col]

	for row in minCostMatrixTable:
		print(row)

	return minCostMatrixTable[rowDest][colDest]

# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCostPath(cost, 2, 2))

# minCostMatrixTable

# [1, 3, 6]
# [5, 9, 5]
# [6, 10, 8]

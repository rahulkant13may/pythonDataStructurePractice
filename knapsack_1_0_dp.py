def knapSack(W, wt, val, n ):
    dp = [[0 for col in range(W + 1)] for row in range(len(val))]
    for row in range(len(val)):
        for col in range(W + 1):
            if col == 0:
                dp[row][col] = 0

            elif row == 0 and  col >= wt[row] and col  != 0:
                dp[row][col] = val[row]

            elif wt[row] > col:
                dp[row][col] = dp[row - 1][col]


            else:
                dp[row][col] = max(dp[row -1][col], val[row] + dp[row - 1][col - wt[row]])

    # print("my")
    # print(dp)
    for x in dp:
        print(x)
    return dp[len(val) - 1][W]


# Driver program to test above function
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
W = 7

# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
n = len(val)
print(knapSack(W, wt, val, n))

   #           0  1  2  3  4  5  6  7

   # (1)   1  [0, 1, 1, 1, 1, 1, 1, 1]
   # (4)   3  [0, 1, 1, 4, 5, 5, 5, 5]
   # (5)   4  [0, 1, 1, 4, 5, 6, 6, 9]
   # (7)   5  [0, 1, 1, 4, 5, 7, 8, 9]

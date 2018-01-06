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

    print("my")
    print(dp)
    return dp[len(val) - 1][W]


# def knapSack(W, wt, val, n):
#     K = [[0 for x in range(W+1)] for x in range(n+1)]
 
#     # Build table K[][] in bottom up manner
#     for i in range(n+1):
#         for w in range(W+1):
#             if i==0 or w==0:
#                 K[i][w] = 0
#             elif wt[i-1] <= w:
#                 K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
#             else:
#                 K[i][w] = K[i-1][w]
#     print(K)
 
#     return K[n][W]

# Driver program to test above function
# val = [1, 4, 5, 7]
# wt = [1, 3, 4, 5]
# W = 7

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))

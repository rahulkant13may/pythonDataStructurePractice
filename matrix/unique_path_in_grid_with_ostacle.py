def uniquePathsWithObstacles(A):

    paths = [[0]*len(A[0]) for i in A]

    if A[0][0] == 0:
        paths[0][0] = 1

    for col in range(1, len(A[0])):
        if A[0][col] == 0:
            paths[0][col] = 1

    for row in range(1, len(A[0])):
        if A[row][0] == 0:
            paths[row][0] = 1

    # adding total paths from top and left
    for row in range(1, len(A[0])):
        for col in range(1, len(A[0])):
            if A[row][col] == 0:
                paths[row][col] = paths[row -1][col] + paths[row][col - 1]

    # return corner value
    return paths[-1][-1]


   

 
# Driver Code
A = [[0, 0, 0], 
     [0, 1, 0], 
     [0, 0, 0]]
print(uniquePathsWithObstacles(A))
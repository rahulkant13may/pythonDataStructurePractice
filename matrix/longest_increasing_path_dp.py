# Author Rahul Kant

R = 4 
C = 4

# return the length of LIP in 2D matrix
def LIP(cost):

    # initialize total length(tl) array
    tl = [[0 for x in range(R)] for x in range(C)]

    # initialize tl[0][0] with 1
    tl[0][0] = 1

    # initialize result with 1
    result = 1


    # Initialize first row of total length(tl) array 
    for col in range(1, C):
        if cost[0][col] > cost[0][col -1]:
            tl[0][col] = tl[0][col - 1] + 1

            
            # update result if current length is greater than result
            if tl[0][col] > result:
                result = tl[0][col]



    # Initialize first column of total length(tl) array
    for row in range(1,R):
        if cost[row][0] > cost[row - 1][0]:
            tl[row][0] = tl[row - 1][0] + 1

            # update result if current length is greater than result
            if tl[row][0] > result:
                result = tl[row][0]

    # Construct rest of the tl array
    for row in range(1,R):
        for col in range(1,C):
            if (cost[row][col] > (cost[row -1][col] or cost[row][col -1])):
                tl[row][col] = max(tl[row - 1][col] , tl[row][col - 1]) + 1

                # update result if current length is greater than result
                if tl[row][col] > result:
                    result = tl[row][col]

    return result


# Driver program to test above functions
if __name__ == "__main__":
    cost = [[1, 2, 3, 4 ],
            [2, 2, 3, 4],
            [3, 2, 3, 4],
            [4, 5, 6, 7]]

    print(LIP(cost))
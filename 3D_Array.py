from numpy import*
arr = array([
            [
                [1,2,3,4],
                [5,6,7,8],    #block1 3*3 2D array
                [4,5,9,0]
            ],
            [
                [4,5,6,7],
                [3,9,1,8],    #block2 3*3 2D array         #Here arr[block][row][col]
                [3,5,7,8]                                  #     arr[3][3][3]
            ],
            [
                [1,2,3,4],
                [3,4,5,6],    #block3 3*3 2D array
                [6,7,8,9]
            ]
            ]
           )
print(arr)

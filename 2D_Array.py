from numpy import*
arr = array([
                [1,3,4],
                [5,7,9]
            ])
print(arr)       #printing 2d array
print(arr.dtype) #what type of data we are working with
print(arr.ndim)  #It will print the dimension of the array
print(arr.shape) #It will print the number of row and col
print(arr.size)  #It will print total number of element
arr1 = arr.flatten() #It will make any array to 1D
print(arr1)

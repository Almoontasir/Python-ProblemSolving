from numpy import*
arr = array([
                [2,3,4,5,5,6],
                [9,8,7,6,4,1]
           ])
arr1 = arr.reshape(2,2,3) # to convert it to 3d must be block*row*col = total element
print("3D")
print(arr1)               # here 2*2*3 = 12
print("1D")
arr2 = arr1.reshape(12)   # making it to 1D Array
print(arr2)
print("2D")
arr3 = arr2.reshape(4,3)  #making it to 2D array
print(arr3)

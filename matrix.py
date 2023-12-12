from numpy import*
arr = array([
            [1,3,2],
            [3,4,6]
      ])
m = matrix(arr)  #creating matrix from 2D array
print(m)
m1 = matrix("2,3,4;3,5,6") #creating a matrix(2*3)
m2 = matrix("2,4;4,3;5,6") #3*2
print(m1)
print(m2)
print(diagonal(m2)) #It will print a diagonal value of a matrix
print(m2.min())     # minimum value of a matrix
print(m2.max())     # maximum value of a matrix
print(m1*m2)        # matrix multiplicaton
m3 = matrix('1,3,4;3,9,1')
print(m1+m3)        #matrix addition

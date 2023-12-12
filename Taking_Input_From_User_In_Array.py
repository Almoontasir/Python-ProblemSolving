from array import *
arr = array('i',[])  #making a empty array
n = int(input("Enter the length of the array"))
for i in range(n):
    x = int(input("Enter values"))
    arr.append(x)
for i in arr:
    print(i,end=" ")            

            


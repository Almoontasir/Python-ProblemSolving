from array import *
arr = array('i',[])
n = int(input("Enter the length of the array "))
print("Enter values one by one ")
for i in range(n):
    x = int(input())
    arr.append(x)
print(arr)
y = int(input("Enter a value to search "))
for j in range(n): #finding the index by linear search
    if arr[j]==y:
        print(j)
        break
    
print(arr.index(y)) #finding the index by using function+-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

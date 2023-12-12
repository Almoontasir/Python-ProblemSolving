from numpy import *
arr = array([0,1])
n = int(input())
for i in range(n-2):
    x = arr[i] + arr[i+1]
    arr = append(arr,x)
print(arr)    
    

    

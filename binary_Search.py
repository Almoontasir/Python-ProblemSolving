from array import *
arr = array('i',[])
n = int(input("Enter the length of the array "))
print("Enter the values one by one ")
for i in range(n):
    x = int(input())
    arr.append(x)
value = int(input("Enter the value to search "))    
l=0
r=n-1
for i in range(n):
    if l<=r:
        m = int((l+r)/2)
        if arr[m]==value:
            print(m)
            break
        elif arr[m]<value:
            l = m+1
        else:
            r = m-1
    else:
        print("The value is not in the array")

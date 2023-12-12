from numpy import *
arr = array([1,2,3,4,5])
print("arr = ",arr)
new_arr1 = arr
print("new_arr1 = ",new_arr1)
new_arr2 = arr.view()
print("new_arr2 = ",new_arr2)
new_arr3 = arr.copy()
print("new_arr3 = ",new_arr3)
print(id(arr))
print(id(new_arr1))
print(id(new_arr2))
print(id(new_arr3))

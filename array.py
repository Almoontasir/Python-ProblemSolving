from array import *
value = array('i',[1,2,3,4,5,6,7])   #creating an array
newvalue = array(value.typecode,(a for a in value))   #copying one array to another
print(value)   #printing the full arry with type
print(newvalue)   #printing the new copy array

for i in value:   #printing the array value one by one
    print(i)
newvalue.reverse()  #reversing the array
print(newvalue)
print(newvalue.typecode)

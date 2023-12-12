from functools import reduce
lst = [3,5,6,9,10,12]
print(lst)
filt = list(filter(lambda a : a%2==0,lst)) #filter will filter values from list by a condition
print(filt)                                #have two arguments one is function and other one is iterable list
double = list(map(lambda a : a*2,lst))  #map will do some operation like double of a list
print(double)                           #have two arguments one is function and other one is iterable list
re = reduce(lambda b,a : b*a,lst)       #reduce will reduce whole list into one value by doing some operation
print(re)                               #have two arguments one is function and other one is iterable list

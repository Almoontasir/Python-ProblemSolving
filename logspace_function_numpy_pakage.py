from numpy import *
a = logspace(0,30,11,endpoint=True,base=9,dtype=int)
print(a)             #here (1)(2)start index and end index is must
print()              #(3)num=number of required value in array,optional,default=50
                     #(4)endpoit = True means stop index inclue False means exclde
                     #(5)retsep = True means difference between values will be visible False means not visible
                     #(6)base = base of log,optional,default = 10
                     #(7)dtype = data type optional,default = int

b = logspace(2,12)   #without optional values
print(b)

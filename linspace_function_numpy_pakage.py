from numpy import *
a = linspace(0,10,3,endpoint=True,retstep=True,dtype='int')
print(a)        #here (1)(2)start index and end index is must
                     #(3)num=number of required value in array,optional,default=50
                     #(4)endpoit = True means stop index inclue False means exclde
                     #(5)retsep = True means difference between values will be visible False means not visible
                     #(6)dtype = data type optional,default = int

b = linspace(2,12)   #without optional values
print(b)
                     

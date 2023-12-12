def update(x):
    print(id(x))
    x = 20
    print(x)
    print(id(x))      #in python there is no call by value or call by reference
                      #changing the value of a variale in function will not effect the the main variable   
    
                      
a = 13
update(a)
print(a)
print(id(a))          

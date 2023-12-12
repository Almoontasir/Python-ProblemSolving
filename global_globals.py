a = 15           #global variable

def somthing():
    a = 10       #local varialble
    print(a)
somthing()    
print(a)

def new_somthing():
    global a     #accessing the global variable
    a = 13       
    print(a)
new_somthing()    
print(a)

def new_somthing1():
    a = 9             #local variable
    x = globals()['a'] #accessing the global variable a
    print(a)
    print(x)
    globals()['a'] = 7  #changing the global variable
new_somthing1()       
print(a)    
    

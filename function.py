def first():
    print("This is my first function in python")

first()

def add(x,y):
    z = x+y
    print(z)
    
add(5,6)

def addition(x,y):
    z = x+y
    return z

result = addition(3,4)
print(result)

def add_sub(x,y):
    z = x+y
    a = x-y
    return z,a

result1,result2 = add_sub(11,4)
print(result1,result2)

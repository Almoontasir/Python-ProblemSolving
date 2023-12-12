def squre(x):
    return x*x
print(squre)
f = squre
print(f(5))

#Higher Order Function

def cube(x):
    return x*x*x
def map_creation(func,new):
    result = []
    for i in new:
        result.append(func(i))
    return result
f = map_creation
print(f(cube,[1,2,3,4,5]))
g = list(map(cube,[1,2,3,4,5]))
print(g)

n = int(input())
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)
    
def work(lst):
    odd,even = 0,0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return odd,even
odd,even = work(lst)
print("even = {} odd = {}".format(even,odd))

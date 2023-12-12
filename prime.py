from math import sqrt
x = int(input("Enter an integer number"))
if x==2 or x==3:
    print("prime number")
elif x==1:
    print("Not prime")
else:
    for i in range(2,int(sqrt(x))):
        if(x%i==0):
            print("Not prime number")
            break
    else:
        print("prime number")
        
    

        

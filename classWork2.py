print("Answer of the first question")
x = 80+10*2
print(x)
x = (80+10)*2
print(x)

print("Ans of the 2nd question")
y = 9>5
print(y)
y = 9>=5
print(y)
y = 9<5
print(y)
y = 9<=5
print(y)
y = 9==5
print(y)
y = 9!=5
print(y)

print("Ans of the 3rd question")
price = 2500
print(price>3000 and price<6000)
price = 50000
print(price>3000 or price<6000)

print("Ans of the 4th question")
temperature = 33
if temperature>30:
    print("It is a hot day")
elif emperature>20:
    print("It is a normal day")
else:
    print("It is a cold day")

print("Answer of the 5th question")
weight= int(input("Weight "))
unit = input("(K) or (L)bs: ")
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight int Lbs: "+str(converted))
else:
    converted=weight*.45
    print("Weight in kg: "+str(converted))

#print("Ans of the 6th question")
#i=1                  I worte the ans in comment 
#while i<=100000:     as the output is taking
    #print(i,end=" ") huge area
    #i = i+1
    
print("Ans of the 7th question(a)")
flowers=["Rose","Daisy","Tulip","Lily","Orchid"]
flowers.append("Gladiolus")
print(flowers)

print("Ans of the 7th question(b)")
flowers.remove("Daisy")
print(flowers)


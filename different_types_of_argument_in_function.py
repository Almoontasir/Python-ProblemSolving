def position(a,b): #here a and b are formal arguments
    c = a+b   
    print(c)
position(3,4)      #here 3 and 4 are the actual arguments and this formet is called position arguments

def keyword(name,age):
    print(name)
    print(age)

keyword(age = 5,name = 'moon') #this is called keyword arguments

def default(name,age = 18):   #this is called default arguments
    print(name)
    print(age)

default("navin")

def variable_length(*b): # here *b is a tuple
    c = 0
    for i in b:
        c = c + i
    print(c)
variable_length(23,45,68) #this is called variable length arguments

def keyword_variable_length(**b): #this is called keyword variable length 
    print(b)
    for i,j in b.items():
        print(i,j)
keyword_variable_length(name = 'moon',age = 23,city = 'panchagarh')        

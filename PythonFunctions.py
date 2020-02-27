#python fuctions
#A function is a block of code which only runs when it is called.

#You can pass data, known as parameters, into a function.

#A function can return data as a result.
#syntax
def add():
    sum= 5+2
    return sum
#call function
add()
print(add())

#other method of calling a function
def add():
    sum= 5+2
    print(sum)
add()

def addition(a,b):
    sum=a+b
    return sum
print(addition(5,10))
print(addition(45,68))



#fuction arguments
print(addition())# this will result to an error since the arguments declared a and b are missing
#requred argument


#defaul argument
def ad(a,b=10):#b=10 is the default argument
    sum=a+b
    return sum
print(ad(120))
print(ad(120,20))#default argument is ignored if two required arguments are provided

#exa,ple 2
def ad(a=10,b=10):#default arguments
    sum=a+b
    return sum
print(ad(500,200))#default arguments are overwritten
print(ad(500,400,23))#result to an error since 3 arguments are provided yet 2 arguments are initialized in the function

#arbitrary argument
def add2(*args):
    sum=a+b+c
    return sum
print(add2(20,21,22))

def students(*names):
    print("student 1 is="+ names[1])

students("john","abdi","mercy")

import math
print("")
print("area of circle")
#function for area of circle
def AreaCircle(r):# r is the argument
    a=r**2*math.pi
    return a
print(AreaCircle(1))
print(AreaCircle(20))
print('')
print("area of triangle")
#Area of triangle
def AreaTriangle(b,h):
    area=0.5*b*h
    return area

#user input b,h
b=float(input("enter the base="))
h=float(input("enter the height="))

print("area of the triangle=",AreaTriangle(b,h))

print("")
print("VOLUME OF CUBOID")
def VolumeCuboid(l,w,h):
    v=l*w*h
    return v

l=float(input("enter the length="))
w=float(input("enter the width="))
h=float(input("enter the height="))

print("volume of the cuboid=",VolumeCuboid(l,w,h))


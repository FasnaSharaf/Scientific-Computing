import math
def Euclidean(x1,y1,z1,x2,y2,z2):
    return (math.sqrt(((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2)))
x1,y1,z1,x2,y2,z2=input("End points of first line followed by space: ").split()
x1=int(x1)
y1=int(y1)
z1=int(z1)
x2=int(x2)
y2=int(y2)
z2=int(z2)
x3,y3,z3,x4,y4,z4=input("End points of second line followed by space: ").split()
x3=int(x3)
y3=int(y3)
z3=int(z3)
x4=int(x4)
y4=int(y4)
z4=int(z4)
if Euclidean(x1,y1,z1,x2,y2,z2)> Euclidean(x3,y3,z3,x4,y4,z4):
    print("First line is longer")
elif Euclidean(x1,y1,z1,x2,y2,z2)< Euclidean(x3,y3,z3,x4,y4,z4):
    print("Second line is longer")
else:
    print("Both are equal in length")
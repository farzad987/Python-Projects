import cmath
a1=int(input("Enter A "))
b1=int(input("Enter B "))
a2=int(input("Enter A "))
b2=int(input("Enter B "))
sign=input("+ or - ")
a3=int(input("Enter A "))
b3=int(input("Enter B "))
A=complex(a1,b1)
B=complex(a2,b2)
C=complex(a3,b3)
    

if sign=="+":
    d= (B**2) - (4*A*C)
    print("Discriminant",d)
elif sign=="-":
    d= (B)**2 + (4*A*C)
    print("Discriminant",d)
else:
    print("Error")

sol1 = (-B-cmath.sqrt(d))/(2*A)
sol2 = (-B+cmath.sqrt(d))/(2*A)
print("First : ",sol1,"\tSecond: ",sol2)
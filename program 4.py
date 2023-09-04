# compute roots of quadric equation
import math
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
d = (b*b) - (4*a*c)
if d >= 0:
    x1 = (-b+math.sqrt(d))/2*a
    x2 = (-b-math.sqrt(d))/2*a
    print("The roots of the given equations are {} and {}".format(x1,x2))
else:
    d = -d
    r = -b/2*a
    img = math.sqrt(d)/(2*a)
    print("x1 = {} + i{}".format(r,img))
    print("x2 = {} - i{}".format(r,img))

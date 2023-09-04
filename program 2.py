#Finding areas of different shapes
#Program2. Compute area of following shapes:
# circle, rectangle, triangle, square, trapezoid and parallelogram.
rad = int(input("Enter the radius for the circle : "))
print("Area of the circle is (radius*radius*3.14) : {}".format(rad*rad*3.14))

leng = int(input("\nEnter the length of the rectangle : "))
width = int(input("Enter the width of the rectangle : "))
print("Area of the rectangle is (length*width) : {}".format(leng*width))

base = int(input("\nEnter the base of the triangle : "))
height = int(input("Enter the height of the triangle : "))
print("Area of the triangle is (0.5*base*height) : {}".format(0.5*base*height))

side = int(input("\nEnter the side of the square : "))
print("Area of the square is (side*side) : {}".format(side*side))

base1 = int(input("\nEnter the first base of trapezoid : "))
base2 = int(input("Enter the second base of trapezoid : "))
height = int(input("Enter the height of the trapezoid : "))
print("Area of the trapezoid is (base1+base2/2)*heigh : {}".format(((base1+base2)/2)*height))

base = int(input("\nEnter the base of parallelogram : "))
height = int(input("Enter the height of parallelogram : "))
print("Area of the parallelogram is (base*height) : {} ".format(base*height))



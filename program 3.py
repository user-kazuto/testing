#Compute the valume of different shapes 
edge = int(input("Enter the edge of the cube : "))
print("Volume of the cube is (edge*edge*edge) : {}".format(edge*edge*edge))

rad = int(input("\nEnter the radius of cylinder : "))
h = int(input("Enter the height of the cylinder : "))
print("Volume of the cylinder is (3.14*rad*rad*h) : {}".format(3.14*rad*rad*h))

r = int(input("\nEnter the radius of the cone : "))
h = int(input("Enter the height of the cone : "))
print("Volume of the cone is ((3.14*r*r)*(h/3) : {}".format(((3.14*r*r)*(h/3))))

r = int(input("\nEnter the radius of the sphere : "))
print("Volume of the sphere is (4/3*3.14*r*r*r) : {}".format((4/3*3.14*r*r*r)))
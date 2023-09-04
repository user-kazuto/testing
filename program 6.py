#check whether the triangle is isosceles or not 
print("If two side of triangle is same then it is isosceles")

side1=int(input("Enter the side1 : "))
side2=int(input("Enter the side2 : "))
side3=int(input("Enter the side3 : ")) 

if(side1==side2 and side1 != side3):
    print("Yes, Triangle is isosceles")
elif(side2==side3 and side2 !=side1):
    print("Yes, Triangle is isosceles")
elif(side1==side3 and side1 !=side2):
    print("Yes, Triangle is isosceles")
else:
    print("No, Triangle is not isosceles")


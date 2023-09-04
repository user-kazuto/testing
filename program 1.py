#Arithmetic operations

print("Here we will use some arithmetic operators ")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

add = num1 + num2
print(" \n {} is the sum of {} and {}".format(add,num1,num2))

sub = num1 - num2
print(" \n {} is the subtraction of {} and {}".format(sub,num1,num2))

multi = num1 * num2
print(" \n {} is the multiplication of {} and {}".format(multi,num1,num2))

division = num1/num2
print(" \n {} is the division of {} and {}".format(division,num1,num2))

exponent = pow(num1,num2)
print(" \n {} is the result of {} to the power {}".format(exponent,num1,num2))
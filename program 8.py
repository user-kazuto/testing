#Sum of natural numbers from 1 to n
num = int(input("Enter the number : "))
add=0
for i in range(1,num+1): 
    add=add+i
    print(i)
print("Sum is : ",add)

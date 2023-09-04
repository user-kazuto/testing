#Printing the table 
print("We are going to print a table ")
num = int(input("\nEnter the number to get its table : "))

for i in range(1,11):
    print("{} X {} = {}".format(num,i,num*i))
#compute (factorial to n)
num = int(input("Enteer the number : "))
fac = 1
for i in range(1,num+1): 
    fac = fac * i
    print(i)
print("Factorial of {} is {}".format(num,fac))
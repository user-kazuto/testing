#print fibonacci numbers upto n
num = int(input("Enter the number : "))
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(1,num+1):
    fibo = num1 + num2
    num1 = num2
    num2 = fibo
    print(fibo)



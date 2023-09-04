'''#we are going to find prime number
num = int(input("Enter the number : "))
k=1
for i in range(2,num+1):
    for j in range(2,num):
        if(i%j != 0):
            print(i)
        
     
    '''
import random
n=int(input("Enter the number of Gamblers : "))
l1=[]
print("Now enter the lucky numbers one by one : ")
for i in range(1,n+1):
    l1.append(int(input()))
print(l1)  
k=1
while(k==1):
    k = int(input("Enter 1 to shuffle and 0 to continue : "))
    random.shuffle(l1)
    print(l1)

new = int(input("Enter the 1 if you wanna gamble else 0 : "))
if(new==1):
    y=random.choice(l1)
    print(y)  
    print("Congratulations you won  : ",y)
else:
    print("bye bye ")


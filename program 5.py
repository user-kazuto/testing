#Program 5. Print numbers up to N which are not divisible by 3,6, 9,, e.g., 1,2,4,5,7,….
#Numbers up to N not divisible by 3, 6 and 9

print("Here we will se numbers which are not divisible by 3, 6 and 9")

num = int(input("Enter the number : "))
for i in range(num+1):
    if (i%3 and i%6 and i%9) != 0:
        print(i)
        

# Count number of persons of age above 60 and below 90
age = []
add = 0
person = int(input("Enter the number of persons : "))
print(f"Now enter the {person} of persons")
for i in range(person):
    age.append(int(input()))
for k in age:
    if (k>60 and k<90):
        add = add+1
print(add)

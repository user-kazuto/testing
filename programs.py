# #print geometric mean and harmonic mean of x
# #  # Get input from the user
# # input_string = input("Enter a series of numbers separated by spaces: ")
# # numbers = [float(x) for x in input_string.split()]

# # # Calculate geometric mean
# # product = 1
# # for num in numbers:
# #     product *= num
# # geometric_mean = product ** (1/len(numbers))

# # # Calculate harmonic mean
# # reciprocal_sum = sum(1/num for num in numbers)
# # harmonic_mean = len(numbers) / reciprocal_sum

# # # Print the results
# # print(f"Geometric Mean: {geometric_mean:.4f}")
# # print(f"Harmonic Mean: {harmonic_mean:.4f}")


# # Get input from the user
# # input_string = input("Enter numbers separated by spaces: ")

# # # Convert the input string into a list of numbers
# # numbers = []
# # current_num = ""
# # for char in input_string:
# #     if char != " ":
# #         current_num += char
# #     else:
# #         if current_num:
# #             numbers.append(float(current_num))
# #             current_num = ""

# # # Handle the last number if it's not followed by a space
# # if current_num:
# #     numbers.append(float(current_num))

# # # Calculate geometric mean
# # product = 1
# # for num in numbers:
# #     product *= num
# # geometric_mean = product ** (1/len(numbers))

# # # Calculate harmonic mean
# # reciprocal_sum = sum(1/num for num in numbers)
# # harmonic_mean = len(numbers) / reciprocal_sum

# # # Print the results
# # print("Geometric Mean:", geometric_mean)
# # print("Harmonic Mean:", harmonic_mean)




# # Get the number of values from the user
# num_values = int(input("Enter the number of values: "))

# # Initialize lists to store the values
# numbers = []
# for i in range(num_values):
#     num = float(input(f"Enter value {i + 1}: "))
#     numbers.append(num)

# # Calculate geometric mean
# product = 1
# for num in numbers:
#     product *= num
# geometric_mean = pow(product, 1/num_values)  # GM = (x1 * x2 * ... * xn)^(1/n)

# # Calculate harmonic mean
# reciprocal_sum = sum(1/num for num in numbers)
# harmonic_mean = num_values / reciprocal_sum  # HM = n / (1/x1 + 1/x2 + ... + 1/xn)

# # Print the results
# print("Geometric Mean:", geometric_mean)
# print("Harmonic Mean:", harmonic_mean)



import itertools

# Create a list of numbers
numbers = [4, 5, 6]

# Generate all possible combinations of length 1 to 3
for r in range(1, len(numbers) + 1):
    combinations = list(itertools.combinations(numbers, r))
    for combo in combinations:        
        print(combo)
 
print("Entered NASA Data base....Successful")





















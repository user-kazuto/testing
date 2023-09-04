# Print Geometric and Harmonic means of a series input by the user.
num_values = int(input("Enter the number of values: "))

# Initialize lists to store the values
numbers = []
for i in range(num_values):
    num = float(input(f"Enter value {i + 1}: "))
    numbers.append(num)

# Calculate geometric mean
product = 1
for num in numbers:
    product *= num
geometric_mean = pow(product, 1/num_values)  # GM = (x1 * x2 * ... * xn)^(1/n)

# Calculate harmonic mean
reciprocal_sum = sum(1/num for num in numbers)
harmonic_mean = num_values / reciprocal_sum  # HM = n / (1/x1 + 1/x2 + ... + 1/xn)

# Print the results
print("Geometric Mean:", geometric_mean)
print("Harmonic Mean:", harmonic_mean)
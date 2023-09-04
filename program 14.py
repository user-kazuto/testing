import itertools
numbers = [4, 5, 6]

# Generate all possible combinations of length 1 to 3
for r in range(1, len(numbers) + 1):
    combinations = list(itertools.combinations(numbers, r))
    for combo in combinations:
        print(combo)
# Create a tuple containing integers
tup = (87, 64, 33, 95, 76)

# Access and print elements at index 0 and index 3
# Index 0 -> first element, Index 3 -> fourth element
print(tup[0], tup[3])  # Output: 87 95

# Find and print the index of the element 33 in the tuple
print(tup.index(33))  # Output: 2 (since indexing starts at 0)

# Calculate and print the sum of all elements in the tuple
print(sum(tup))  # Output: 355

# Find and print the smallest element in the tuple
print(min(tup))  # Output: 33

# Find and print the largest element in the tuple
print(max(tup))  # Output: 95

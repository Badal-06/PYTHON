# Create an empty set named 'coll'
coll = set()

# Add a string element to the set
coll.add("badal")

# Add a number to the set
coll.add(90)

# Remove the number 90 from the set
coll.remove(90)

# Clear all elements from the set (now 'coll' is empty)
coll.clear()

# Add the number 9 to the set
coll.add(9)

# Print the current elements of the set
print(coll)  # Output: {9}

# Remove and return a random element from the set (since sets are unordered)
print(coll.pop())

# Print the type of 'coll' to confirm it is a set
print(type(coll))

# Create two sets for set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of two sets (combines elements without duplicates)
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection of two sets (common elements in both)
print(set1.intersection(set2))  # Output: {3, 4}

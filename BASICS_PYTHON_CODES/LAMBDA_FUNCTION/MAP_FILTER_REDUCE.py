from functools import reduce   # Import reduce function from functools module

# A list of numbers
num = [1, 2, 3, 4, 5]

# Use map() with a lambda function to calculate squares of each number in the list
squares = list(map(lambda x: x**2, num))

# Use filter() with a lambda function to get only even numbers from the list
even = list(filter(lambda x: x % 2 == 0, num))

# Use reduce() with a lambda function to calculate the product of all numbers in the list
products = reduce(lambda x, y: x * y, num)

# Print the results
print("Squares of numbers:", squares)
print("Even numbers are:", even)
print("Product of numbers is:", products)
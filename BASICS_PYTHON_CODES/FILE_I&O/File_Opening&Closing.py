# Open the file named "hello" in read mode ("r")
f = open("hello", "r")

# Read the entire content of the file and store it in the variable 'data'
data = f.read()

# Print the content of the file
print(data)

# Close the file to free up system resources
f.close()
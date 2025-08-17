# First, you need to create a file named "Test.txt" in the same directory.

# Open the file "Test.txt" in read mode ('r') with UTF-8 encoding
f = open('Test.txt', mode='r', encoding='utf-8')

# Print the name of the file
print("File Name:", f.name)

# Print the mode in which the file was opened (e.g., 'r', 'w', etc.)
print("File Mode:", f.mode)

# Print whether the file is readable (should return True in 'r' mode)
print("File Readable:", f.readable)

# Print whether the file is writable (should return False in 'r' mode)
print("File Writable:", f.writable)

# Print whether the file is currently closed (False because it's open)
print("File closed:", f.closed)

# Close the file to release system resources
f.close()

# Print again to check that the file is now closed (should return True)
print("File Closed:", f.closed)
# Create a dictionary 'stud' to store student information
stud = {
    "name": "badal",   # Student's name
    "cgpa": 9.7,       # Student's CGPA
    "sub": {           # Nested dictionary for subject marks
        "chem": 90,    # Chemistry marks
        "phy": 80,     # Physics marks
        "math": 95,    # Mathematics marks
    }
}

# Add a new key-value pair "course": "b.tech" to the dictionary
# .update() modifies the dictionary in place and returns None
stud.update({"course": "b.tech"})  

# Correctly get Chemistry marks from inside the 'sub' dictionary
print(stud["sub"]["chem"])  # Output: 90

# Print all dictionary items (key-value pairs) as a list of tuples
print(stud.items())

# Print all the values in the dictionary
print(stud.values())

# Print all the keys in the dictionary
print(stud.keys())

# Access and print the 'math' marks from the nested dictionary 'sub'
print(stud["sub"]["math"])

# Print the type of 'stud' to confirm it's a dictionary
print(type(stud))

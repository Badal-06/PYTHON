# Dictionary storing usernames as keys and passwords as values
user_data = {
    "badal": "0000",
    "harsh": "1111",
    "nevid": "2222",
    "prince": "3333",
    "ricky": "4444",
    "sahil": "5555",
    "thor": "6666",
    "hulk": "7777",
    "wanda": "8888",
    "elon": "9999"
}

# Ask the user to enter their username
username = input("Enter your username: ")

# Ask the user to enter their password
password = input("Enter your password: ")

# Check if the username exists and the password matches
if username in user_data and user_data[username] == password:
    # If both username exists and password is correct
    print("Login successful! ")

# If username exists but password is wrong
elif username in user_data:
    print("Incorrect password! ")

# If username is not found in the dictionary
else:
    print("Username not found! ")
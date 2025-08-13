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
username = input("Enter your username: ")
password = input("Enter your password: ")

if username in user_data and user_data[username] == password:
    print("Login successful! ")
elif username in user_data:
    print("Incorrect password! ")
else:
    print("Username not found! ")
str=input("Enter the string:")
no_of_alphabets=0
no_of_digits=0
for i in range(len(str)):
    char=str[i]
    if char.isalpha():
        no_of_alphabets+=1
    elif char.isdigit():
        no_of_digits+=1
    i+=1
print(f"No. of alphabets in the given string:{no_of_alphabets}")
print(f"No. of Digits in the given string:{no_of_digits}")

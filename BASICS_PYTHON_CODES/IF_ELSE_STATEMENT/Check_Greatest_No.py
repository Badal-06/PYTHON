# Take four integer inputs from the user
a = int(input("Enter your first num = "))
b = int(input("Enter your second num = "))
c = int(input("Enter your third num = "))
d = int(input("Enter your fourth num = "))

# Check if 'a' is greater than b, c, and d
if (a > b and a > c and a > d):
    print("First num is the greatest", a)

# If the above is false, check if 'b' is greater than c and d
elif (b > c and b > d):
    print("Second num is the greatest", b)

# If the above is false, check if 'c' is greater than d
elif (c > d):
    print("Third num is the greatest", c)

# If none of the above is true, 'd' must be the greatest
else:
    print("Fourth num is the greatest", d)

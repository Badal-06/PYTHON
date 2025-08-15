# Traffic light simulation program

# Take input for the traffic light color from the user
# Convert the input to lowercase so it works regardless of how the user types it (e.g., "Red", "RED", "red")
light = str(input("light: ")).lower()

# If the light is red, instruct to stop
if light == "red":
    print("stop")

# If the light is yellow, instruct to look/wait
elif light == "yellow":
    print("look")

# If the light is green, instruct to go
elif light == "green":
    print("go")

# If the input does not match any known light color, print an error message
else:
    print("light is broken")

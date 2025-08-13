def check_element_exists(tup, element):
    return element in tup

# Example tuple
my_tuple = (10, 20, 30, 40, 50)

# Element to check
element = 30

# Check and print result
if check_element_exists(my_tuple, element):
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

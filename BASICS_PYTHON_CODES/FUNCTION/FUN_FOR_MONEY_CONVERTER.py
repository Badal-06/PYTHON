# Function to convert USD to INR
def convereter(usd_val):
    # Convert USD to INR using a fixed conversion rate (1 USD = 83 INR)
    inr_val = usd_val * 83
    # Print the result in a readable format
    print(usd_val, "usd =", inr_val, "inr")

# Call the function with 100 USD as input
convereter(100)

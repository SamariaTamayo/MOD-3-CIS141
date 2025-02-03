# Ask the user for the order total
order_total = float(input("Enter the order total: $"))

# Determine if shipping applies and calculate the total cost
if order_total < 50:
    shipping_cost = 5  # $5 shipping for orders under $50
else:
    shipping_cost = 0  # Free shipping for orders $50 or more

# Calculate the total cost
total_cost = order_total + shipping_cost

# Print the total cost, including shipping
print(f"The total cost, including shipping, is: ${total_cost:.2f}")


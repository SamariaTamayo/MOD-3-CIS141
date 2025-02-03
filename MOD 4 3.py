# Prompt the user for their bank balance
balance = float(input("Enter your bank balance: "))

# Check if the balance is less than $100
if balance < 100:
    print(True)  # If balance is below $100, print True
else:
    print(False)  # Otherwise, print False

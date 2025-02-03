# Constructing the truth table for the expression: (A AND B) OR (NOT B)

print("A\tB\t(A AND B) OR (NOT B)")  # Printing the header of the table

# Looping through all possible combinations of A and B
for A in [True, False]:
    for B in [True, False]:
        result = (A and B) or (not B)  # Evaluate the expression
        print(f"{A}\t{B}\t{result}")  # Print the values of A, B, and the result

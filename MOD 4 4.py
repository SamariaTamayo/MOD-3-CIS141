# Prompt the user for their age
age = int(input("Enter your age: "))

# Check the age group and print the appropriate movie rating
if age < 13:
    print("You can see G-rated movies.")
elif 13 <= age <= 17:
    print("You can see PG-13 rated movies.")
else:
    print("You can see R-rated movies.")

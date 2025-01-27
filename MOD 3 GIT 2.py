# Prompt the user for their name and age
name = input("What is your name? ")
age = int(input("How old are you? "))

# Calculate the age next year
next_year_age = age + 1

# Use string methods to manipulate the string (example: capitalize name and split it)
name = name.capitalize()  # Capitalize the first letter of the name

# Create a sentence using string concatenation
sentence = "Hello, " + name + "! You are " + str(age) + " years old. Next year, you will be " + str(next_year_age) + " years old."

# Use .split() to turn the sentence into a list of words
sentence_words = sentence.split()

# Use .join() to join the list back with a space separator
formatted_sentence = " ".join(sentence_words)

# Print the sentence using custom separator and end
print(formatted_sentence, end=".\n")# Write your code here :-)

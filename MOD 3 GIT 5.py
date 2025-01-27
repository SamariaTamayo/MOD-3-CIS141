# Write your cod# Prompt the user for three words
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")

# Use .split() to break the words into a list (though not strictly necessary here)
words = [word1, word2, word3]

# Optionally modify words using .replace() (for example, change lowercase 'a' to uppercase 'A')
modified_words = [word.replace("a", "A") for word in words]

# Use .join() to combine the words with a '|' separator
joined_words = "|".join(modified_words)

# Print the joined words with the custom separator and end using print() keyword arguments
prnit(joined_words, end=".\n")e here :-)

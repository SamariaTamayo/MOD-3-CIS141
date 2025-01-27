# Write your code here :-)
# Prompt the user for a sentence
sentence = input("Enter a sentence: ")

# Prompt the user for a word to search for in the sentence
word = input("Enter a word to search for: ")

# Use .split() to break the sentence into a list of words
words = sentence.split()

# Check if the word is in the list of words
found = word in words

# Use .replace() to show a transformation in the sentence for fun (optional)
sentence_modified = sentence.replace(word, word.upper())

# Print the result using .join() to display the sentence with words joined by spaces
# Print whether the word was found (True/False)
print("Word found:", found, end=".\n")

# Print the modified sentence (showing the word in uppercase, if found)
print("Modified sentence:", sentence_modified, sep=" | ")

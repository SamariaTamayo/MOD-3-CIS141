# Write your code here :-)
# Prompt the user for a word
word = input("Enter a word: ")

# Prompt the user for the first index
first_index = int(input("Enter the first index: "))

# Prompt the user for the last index
last_index = int(input("Enter the last index: "))

# Slice the word at the provided indexes
sliced_word = word[first_index:last_index]

# Use .replace() to show an example transformation (optional)
sliced_word_modified = sliced_word.replace("a", "A")

# Use .split() to split the sliced word into individual characters (as an example)
sliced_word_list = list(sliced_word)

# Use .join() to reassemble the sliced word with a custom separator (for demonstration)
reassembled_sliced_word = "|".join(sliced_word_list)

# Print the sliced word
print("Sliced word:", sliced_word, end=".\n")

# Print the modified sliced word (e.g., with 'a' replaced by 'A')
print("Modified sliced word:", sliced_word_modified, sep=" | ")

# Print the reassembled sliced word with "|" separator
print("Reassembled sliced word:", reassembled_sliced_word, sep=" | ")

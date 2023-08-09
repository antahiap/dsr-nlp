import re

# Read the content of the text file
with open("data/lsdyna_ii_r13.txt", "r") as file:
    text = file.read()

# Define the regex pattern
pattern = r'\bMAT_\w+\b'

# Find all matches in the text
matches = re.findall(pattern, text)


with open("data/word_list.py", "w") as file:
    file.write("word_list_MAT = " + str(matches))

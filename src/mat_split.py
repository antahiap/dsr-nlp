import re
from tqdm import tqdm

# Read the content of the text file
with open("data/lsdyna_ii_r13.txt", "r") as file:
    text = file.read()

# Define the regex pattern
mat_pattern = r'\bMAT_\w+\b'

# Find all matches in the text
mat_list = re.findall(mat_pattern, text)


for mat in tqdm(mat_list):
    pattern =  re.escape(mat) + "(.*?)MAT_" 
    mat_text = re.findall(pattern, text, re.DOTALL)
    mat_text = '. '.join(mat_text)

    out_path = f'data/mat/{mat}.txt'
    with open(out_path, "w",encoding="utf-8") as output_file:
        output_file.write(mat_text)
    
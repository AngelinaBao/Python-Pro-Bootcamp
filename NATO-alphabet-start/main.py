import pandas as pd

nato_df = pd.read_csv("./NATO-alphabet-start/nato_phonetic_alphabet.csv")

# 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Please input a name: ").upper()
code_list = [nato_dict[char] for char in user_input]

print(code_list)

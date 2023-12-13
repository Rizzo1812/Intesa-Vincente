import json
import random

def capitalize_first_letter(word):
    return word.capitalize()

def txt_to_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        # read lines and remove blank spaces
        parole = [line.strip() for line in txt_file.readlines()]

    # shuffle words
    random.shuffle(parole)

    # Make first letter of each word uppercase
    parole_maiuscole = list(map(capitalize_first_letter, parole))

    with open(output_file, 'w', encoding='utf-8') as json_file:
        # Scrivi la lista di parole maiuscole e mescolate nel file JSON
        json.dump(parole_maiuscole, json_file, ensure_ascii=False, indent=2)

# filename of input and output files
input_filename = 'parole.txt'
output_filename = 'parole.json'

# function call to convert txt to json file
txt_to_json(input_filename, output_filename)

print(f'Converted! File "{output_filename}" created.')

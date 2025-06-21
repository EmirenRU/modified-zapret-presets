# The script is created by Emiren
# It utilizes a set container to contain all unique names, which leads to shuffle
# To run script, execute `python file.py` from the directory, for example, /lists

import os

def get_lists_of_files(directory):
    txt_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            txt_files.append(os.path.join(directory, filename))
    return txt_files

def remove_duplicate_linse(f):
    seen = set()

    with open(f, 'r') as file:
        for line in file:
            sl = line.strip()
            if sl not in seen:
                seen.add(sl)
    
    with open(f, 'w') as file:
        for line in seen:
            file.write(line + '\n')


if __name__ == "__main__":
    files = get_lists_of_files(os.getcwd())
    for file in files:
        remove_duplicate_linse(file)
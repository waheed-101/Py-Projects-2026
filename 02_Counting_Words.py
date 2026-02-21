''' Word Counter - Counts word frequency in a text file
This script reads a text file and counts how many times each word appears. '''


import string

file_name = input("Enter the file name: ")
# If user just hits enter, use default filename
if len(file_name) < 1:
    file_name = "Text_File.txt"

try:
    with open(file_name, 'r') as file:
        my_dict = dict()

        for line in file:
            line = line.rstrip()
            words = line.split()

            for word in words:
                # Remove punctuation from the word and convert to lowercase, if needed.
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()

                # skip empty strings
                if not word:
                    continue

                if word in my_dict:
                    my_dict[word] += 1
                else:
                    my_dict[word] = 1
        print(f"\n\nWord Frequency Count:\n{my_dict}\n\n")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
# Dia 27: https://www.youtube.com/watch?v=V87m9SltcI8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=37
# external files

from io import open  # NOTE: this method will create the file if it doesn't exist'


text_file = open('file.txt', 'w') ## write

phrase = 'excellent day for studying Python \non Saturday'

text_file.write(phrase)

text_file.close()


## here we will read the file
text_file = open('file.txt', 'r') ## read

text = text_file.read()

text_file.close()

# print(text)

## Read line by line and creates a list
text_file = open('file.txt', 'r') 

lines_text = text_file.readlines()

text_file.close()

# print(lines_text)

# print(lines_text[0])

## add more lines into our file

text_file = open('file.txt', 'a') ## append

text_file.write('\nis always a good thing')

text_file.close()
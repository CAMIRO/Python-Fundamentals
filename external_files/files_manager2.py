# Dia 28: https://www.youtube.com/watch?v=V87m9SltcI8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=38
# external files

from io import open  


## here we will read the file
text_file = open('file.txt', 'r')

print(text_file.read())

text_file.seek(0) ## seek will move the cursor to the beginning

print(text_file.read())


## read accept a parameter
text_file.seek(0)
print(text_file.read(6)) # it will read til the 10 position





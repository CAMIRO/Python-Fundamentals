# Dia 28: https://www.youtube.com/watch?v=V87m9SltcI8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=39
# Python object serialization

import pickle 

names_list = ['Peter', 'Anna', 'John', 'Maria']

# creates the external file
binary_file = open('names_list', 'wb') # wb = write binary


# Dumping the list into a file (dumping = volcado)
pickle.dump(names_list, binary_file)

binary_file.close()

# delete the binary_file from memory
del (binary_file)






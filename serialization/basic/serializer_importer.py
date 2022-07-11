# Dia 28: https://www.youtube.com/watch?v=V87m9SltcI8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=39
# Python object serialization

import pickle

file =open('names_list', 'rb') # read binary

names_list = pickle.load(file)

print(names_list)
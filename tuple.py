# Dia 5

# Tuplas

myTuple=(1,2,3,'anotherOne',1)
print(myTuple[2:])

# Comber Tuple to list and vice versa
myList=list(myTuple) ## same goes vice versa: tuple()
print(myList)

# find a member in the Tuple
print(1 in myTuple)

# Counts how many times the element is in the tuple
print(myTuple.count(1))

# Length of the tuple
print(len(myTuple))

# Unitary Tuple
anotherTuple=('element',) # dont forget the last comma at the end

# Unpacking a tuple
thirdTuple=('Juan',13,1,1991)
name, day, month, year=thirdTuple
print(name, year)






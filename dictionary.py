# Dia 6

# Dictionaries

my_dictionary = {
    "France":"Paris", 
    "Germany":"Berlin",
    "Italy":"Rome", 
    "Spain": "Madrid"
}
## add a new element to the dictionary
my_dictionary["United Kingdom"]="Manchester"
print(my_dictionary)
print(my_dictionary["France"])

## rewrite an element in the dictionary
my_dictionary["United Kingdom"]="London"
print(my_dictionary)

## Remove an element from the dictionary
del my_dictionary["France"]
print(my_dictionary)

#Can add different types of values:
another_dictionary = {
    "France":"Paris",
    23: "Jordan",
    "Mosqueteros": 3
}

## adding a tuple to the dictionary:

my_tuple =("Spain", "France", "Germany")
dictionary={
    my_tuple[0]:"Madrid",
    my_tuple[1]:"Paris",
    my_tuple[2]:"Berlin",
}
print("dictionary: ", dictionary)

## adding a whole tuple into a key dictionary value:


player_dictionary={
    23: "jordan",
    "name": "Michael",
    "team": "Chicago",
    "years": ["2008", "2009", "2010", "2011"]
}

print("player_dictionary: ", player_dictionary)
print("player_dictionary -> years: ", player_dictionary["years"])

## We can add a dictionary to another dictionary

player_dictionary={
    23: "jordan",
    "name": "Michael",
    "team": "Chicago",
     "years": {
        "seasons": ["2008", "2009", "2010", "2011"]
     }
}

print("dictionary inside dictionary: ", player_dictionary)

## Access to dictionary keys:
print(player_dictionary.keys())

## Access to dictionary values:
print(player_dictionary.values())

## Length of a dictionary 
print(len(player_dictionary))
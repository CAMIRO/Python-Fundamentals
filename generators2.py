# Dia 14

# Yield from


# Yield from works as simplify the code for generators in case
# we have to use nested loops (bucles anidados) Ej: for loop within another for loop

# Example One without the from: 

def cities_generator(*cities): # the * in the parameter means that it will get an undefined number of elements and they will come as a tuple
    for city in cities:
        for sub_item in city:
            yield sub_item

returned_cities = cities_generator('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(returned_cities))
print(next(returned_cities))


# Example Two with the from: 

def cities_generator(*cities): # the * in the parameter means that it will get an undefined number of elements and they will come as a tuple
    for city in cities:
        # for sub_item in city:
            yield from city # yield desde (from) el primer elemento

returned_cities = cities_generator('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(returned_cities))
print(next(returned_cities))













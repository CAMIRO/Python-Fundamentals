# Dia 13


# Example: 
def generator():
    value = 0
    # logic here
    yield value

generator()


# Example 2: 

#2.A Normal function :
def even_generator_func(limit):
    num = 1
    my_list=[]

    while num <= limit:
        my_list.append(num *2)
        num = num + 1

    return my_list

print(even_generator_func(10))


#2.B Generator function:

## Because generator return a iterable list at the end. we dont need to declare an empty list
def cities_generator(*cities): # the * in the parameter means that it will get an undefined number of elements and they will come as a tuple
    for city in cities:
        yield city

returned_cities = cities_generator('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(returned_cities))
print(next(returned_cities))


# Another Example: 
# def even_generator_generator(limit):
#     num = 1
#     while num < limit:
#         yield num * 2 # it is adding a value one by one. so it stops every iteration. (suspe    nsion state)
#         num = num + 1

# returned_even_values = even_generator_func(10)

# # print(returned_even_values)


# ### We can see the use of yield in action with the following code:

# print(next(returned_even_values)) # dont know why it dosent work but next Example it does
# print(next(returned_even_values))





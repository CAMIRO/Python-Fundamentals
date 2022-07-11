# Dia 4

# Listas son iguales a los Arrays

name_list = [ True, 'hello', 1.45, 8 ]

## Full list printed
print(name_list[:])

## Specific list member
print(name_list[0])

## Reverse specific list member
print(name_list[-1])

## Portion list members
print(name_list[0:2]) ### Can also do: print(name_list[:2])

## add a member at the end as push() in JS:
name_list.append('new_member')
print(name_list[:])

## add a member in a specific index:
name_list.insert(2, 'new_member_two')
print(name_list[:])

## add multiple members:
name_list.extend(['new_member_three', 'new_member_four'])
print(name_list[:])

## give a index member
print(name_list.index(8))

## find a member in a list 
print('new_member' in name_list)

## remove a member
name_list.remove(1.45)
print(name_list[:])

## remove the last member:
name_list.pop()
print(name_list[:])


## add two different Lists:
my_list_one = [1,2]
my_list_two = [3,4]

my_list_three = my_list_one + my_list_two
print(my_list_three)

## multiply a list: 
my_list_five = [1,2]* 3

print(my_list_five)


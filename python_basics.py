# Dia 1
a = 0

for i in range(5):
    a+=1
    print(a)

# Dia 2

## Variables
name = ''
my_name = ''

print(type(name))

### Everything on python is an object

message = """This is a message 
that has 
three line texts
"""

print(message)

### Comparing methods

number_one = 5
number_two = 7

if number_one > number_two:
    print('Number One is bigger')
else:
    print('Number Two is bigger')

# Dia 3

## Function: basic structure
def name_function():
    # return (optional)
    pass


def sum(num1, num2):
    result = num1 + num2
    print(result)
    return result

sum(1,2)
sum(3,8)
save_result=sum(1,9)





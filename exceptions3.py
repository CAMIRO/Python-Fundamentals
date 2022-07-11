# Dia 17

# Raise exceptions (Create own exceptions)
def eval_age(age):

    if age < 0:
        raise TypeError("can use negative values") 

    if age < 20:
        return 'too young'
    elif age < 40:
        return 'young'
    elif age < 65:  
        return 'old' 
    elif age < 100:  
        return 'very wise'  

print(eval_age(-18))


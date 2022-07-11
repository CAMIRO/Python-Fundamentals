# Dia 18

# class:
class Car():
    # Properties
    length_chassis=250
    width=120
    wheels=4
    is_on=False

    # Methods
    def start_up(self):
        self.is_on=True     # this is equivalent to: myCar.is_on=True 
    
    def status(self):
        if(self.is_on):
            return 'its on!'
        else:
            return 'its off!'


# Object | instance
myCar = Car() ## We are instantiating a class (NOTE: no need to add the keyword "new" as in JS)

## accessing to an object property: 
print(myCar.length_chassis)

## execute an object method:
myCar.start_up() ## NOTE: myCar is now 'self'

print(myCar.status())

 



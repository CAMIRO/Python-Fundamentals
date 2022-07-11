# Dia 19

# class:
class Car():
    # initial state (AKA: constructor)
    def __init__(self):
        self.__length_chassis=250
        self.__width=120
        # NOTE: Encapsulation: adding __ will encapsulate the property protecting it to be modified outside the class
        self.__wheels=4
        self.__is_on=False
 
    def start_up(self, init):
        self.__is_on = init
        if(self.__is_on):
            return 'its on!'
        else:
            return 'its off!'   
    
    def status(self):
        print(f'Car has {self.__wheels} wheels. a length of {self.__length_chassis} and with {self.__width}')


# Object | instance
myCar = Car()

print(myCar.start_up(True))
myCar.status()

print('-------------- another car object ---------------')

# Another  Object | instance
myCar2 = Car()

myCar2.__wheels=2 # although i tried to modified outside the class, it didn't work.
print(myCar.start_up(False))
myCar2.status()


 



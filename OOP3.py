# Dia 20

# class:
class Car():
    def __init__(self):
        self.__length_chassis=250
        self.__width=120
        self.__wheels=4
        self.__is_on=False
 
    def start_up(self, init):
        self.__is_on = init

        if self.__is_on:
            check = self.__inner_check()

        if(self.__is_on and check):
            return 'its on!'
        elif(self.__is_on and check==False):
            return 'Something when wrong after the checking'
        else:
            return 'its off!'   
    
    def status(self):
        print(f'Car has {self.__wheels} wheels. a length of {self.__length_chassis} and with {self.__width}')

    def __inner_check(self):                    # NOTE: Encapsulate inner method
        print('Doing inner check...')

        self.fuel='ok'
        self.oil='ok'
        self.doors='ok'

        if(self.fuel=='ok' and self.oil=='ok' and self.doors=='ok'):
            return True
        else:
            return False




# Object | instance
myCar = Car()

print(myCar.start_up(True))
myCar.status()

# print(myCar.__inner_check()) ---- this wont work, cuz is now a private method

print('-------------- another car object ---------------')

# Another  Object | instance
myCar2 = Car()

print(myCar.start_up(False))
myCar2.status()


 



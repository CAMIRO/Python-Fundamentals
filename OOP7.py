# Dia 23: https://www.youtube.com/watch?v=kV1cN_bqcSw&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=32
# Polimorfismo - polymorphism: 

class Car():
    def move(self):
        print('move using 4 wheels')

class MotorBike():
    def move(self):
        print('move using 2 wheels')

class Truck():
     def move(self):
        print('move using 6 wheels')



def vehicleMove(vehicle):  ## NOTE: Adding a function and passing the object as a
                           ## parameter its all it takes to make a polymorphism object and has access to its individual properties and methods.
    vehicle.move()

myVehicle = Truck()


vehicleMove(myVehicle)
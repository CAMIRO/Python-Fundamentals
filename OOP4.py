# Dia 21: https://www.youtube.com/watch?v=u_VbLsIyzRk&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=29
# Herencia - Inheritance: 

# super class || parent class
class Vehicles():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False
        self.accelerate = False
        self.brake = False

    def start_up(self):
        self.is_on = True

    def accelerating(self):
        self.accelerate = True

    def braking(self):
        self.brake = True

    def status(self):
        print(f'Brand: {self.brand} \nModel: {self.model} \nIs on: {self.is_on} \nBrake: {self.brake} \nAccelerator: {self.accelerate}')


# Subclass || child class
class Motorcycle(Vehicles): ## THIS IS ALL YOU NEED TO DO TO DO INHERITANCE
    pass

## Object
MyMotorcycle = Motorcycle('Honda', 'CBR')

MyMotorcycle.status() 
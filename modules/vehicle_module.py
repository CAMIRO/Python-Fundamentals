# Dia 25: https://www.youtube.com/watch?v=t93x-vnFvP4&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=34 
# Modules



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
        print(f'Brand: {self.brand} \nModel: {self.model} \nIs on: {self.is_on} \nBrake: {self.brake} \nAccelerator: {self.accelerate} \n')

# another Subclass
class Van(Vehicles):
    def cargo(self, cargo):
        self.max_cargo =cargo
        if self.max_cargo:
            return 'The cargo van is full'
        else:
            return 'The cargo van is not full'

# Subclass || child class
class Motorcycle(Vehicles): 
    drive_with_one_wheel=''
    def one_wheel(self):
        self.drive_with_one_wheel = 'Driving with one wheel'

    def status(self): ## NOTE: Local method status will overwrite Super class method status
        print(f'Brand: {self.brand} \nModel: {self.model} \nIs on: {self.is_on} \nBrake: {self.brake} \nAccelerator: {self.accelerate} \nOne wheel: {self.drive_with_one_wheel} \n')

# Another super class || parent class
class ElectricVe(Vehicles):
    def __init__(self, brand, model,):

        super().__init__(brand, model)

        self.autonomy = 100

    def ChargeBattery(self):
        self.Charging = True



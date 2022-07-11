# Dia 29: https://www.youtube.com/watch?v=V87m9SltcI8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=40
# Python object serialization

import pickle



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


car1=Vehicles('Mazda','MX5')
car2=Vehicles('Ferrari','Maranello')
car3=Vehicles('Renault','Spark')

cars=[car1, car2, car3]

file=open('the_cars', 'wb')
pickle.dump(cars, file)

file.close()
del (file)




### Step 2

file_open =open('the_cars', 'rb')

my_cars=pickle.load(file_open)

file_open.close()

for c in my_cars:
    print(c.status())


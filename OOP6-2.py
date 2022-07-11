# Dia 22: https://www.youtube.com/watch?v=oe04X1B14YY&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=31
# Herencia - Inheritance: 
## functions>> super() - isinstance()

# Super class
class Person():
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address    
    
    def description(self):
        print(f'Name: {self.name}, Age: {self.age}, Address: {self.address}')

# Sub class
class Employee(Person):
    def __init__(self,salary, years, name_employee, age_employee, address_employee):

        super().__init__(name_employee, age_employee, address_employee) ## NOTE: super() is calling the parent class method (in this case __init__). this allows to import parents methods into child classes
                           ## another thing to noticed, is that it will execute the parent constructor be anything else.             
        self.salary = salary
        self.years = years

    
    def description(self):

        super().description()   ## Doing the super() again!

        print(f'Salary: {self.salary}, Years: {self.years}')


Max = Employee(1500, 2, 'Max', 24, 'France')
Max.description()



# python method that allows us to find if a class is a subclass of another class

Jay = Person('Jay', 55, 'Argentina')

print(isinstance(Max, Employee))
print(isinstance(Max, Person))


print(isinstance(Jay, Employee))
print(isinstance(Jay, Person))




    


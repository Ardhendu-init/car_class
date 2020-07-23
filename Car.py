# A simple example of a car class
class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
        self.run = 0

    def description(self):
        print(f"Company name :{self.company.capitalize()}\nModel name:{self.model.capitalize()}\nYear:{self.year}")

    def run_so_far(self, a):  # In this method i added a parameter because distance covered is not constant
        self.run = a

    def odometer(self):
        print(f'The car has so far run: {self.run} kms')


# creating a completely different class  as Battery as every car should not have the attribute battery

class Battery:
    def __init__(self, battery=70):
        self.battery = battery

    def battery_details(self):
        if 70 <= self.battery <= 120:
            print(f'The battery Power = {self.battery} kwh ,It is in good condition')
        else:
            print("You need to change the battery")

# creating a child class using magic method too (inheritance)


class Solar(Car):
    def __init__(self, company, model, year):
        super().__init__(company, model, year)
        self.battery = Battery

    def solar_car(self):
        print(f'The solar car name:{self.company}\nModel:{self.model}\nYear: {self.year} ')


c = Solar('Photon', 'Helium', 20)
c.description()
c.battery().battery_details()
c.run_so_far(120)
c.odometer()

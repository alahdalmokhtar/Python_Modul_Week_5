# the main class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make        
        self.model = model      
        self.year = year        

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

#for the road vehicles
class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive  #push the four wheel

    def display_info(self):
        super().display_info()
        print(f"Four Wheel Drive: {self.four_wheel_drive}")

#      inheritance for the sports cars from the vehicles
class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed 

    def display_info(self):
        super().display_info()
        print(f"Max Speed: {self.max_speed} km/h")

# cerate instances of the classes
suv = OffRoadVehicle("Toyota", "Land Cruiser", 2022, True)
sports_car = SportsCar("Ferrari", "488 GTB", 2021, 330)

# print the information of the vehicles
print("Off-Road Vehicle Info:")
suv.display_info()

print("\nSports Car Info:")
sports_car.display_info()

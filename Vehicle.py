class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Off_Road_Vehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

class SportCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.top_speed = max_speed


off_road_vehicle = Off_Road_Vehicle("Toyota", "Land Cruiser", 2020, True)
sport_car = SportCar("Ferrari", "488", 2021, 211)
print(f"Off-Road Vehicle: {off_road_vehicle.make} {off_road_vehicle.model}, Year: {off_road_vehicle.year}, 4WD: {off_road_vehicle.four_wheel_drive}")
print(f"Sport Car: {sport_car.make} {sport_car.model}, Year: {sport_car.year}, Top Speed: {sport_car.top_speed} mph")

    
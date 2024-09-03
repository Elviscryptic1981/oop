class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    all_cars = []
    car_count = 0

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        Car.add_car(self)

    def start(self):
        print(f"{self.brand} {self.model} Car started.")

    @classmethod
    def add_car(cls, car):
        cls.all_cars.append(car)
        cls.car_count += 1
        return cls.all_cars
    
    @classmethod
    def get_all_cars(cls):
        return cls.all_cars

Honda = Car("Honda", "CR-V")
Toyota = Car("Toyota", "Camry")

Honda.start()
Toyota.start()

print([f"{car.brand} {car.model}" for car in Car.get_all_cars()])
print(f"Total cars: {Car.car_count}")

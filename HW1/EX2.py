import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def logger(method):
    @wraps(method)
    def wrapper(self):
        class_name = self.__class__.__name__
        result = method(self)
        logging.info(f"The {class_name} {result}\n")
        return result
    return wrapper

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @logger
    def drive(self):
        return(f"{self.brand} is vehicle ")

class Car(Vehicle):
    @logger
    def drive(self):
        return(f" {self.brand}  is driving on the road at {self.speed} km/h.")


class Boat(Vehicle):
    @logger
    def drive(self):
        return(f" {self.brand}  is sailing at sea at {self.speed} knots.")

# === Main Program ===
if __name__ == "__main__":
    car = Car("Toyota", 120)
    boat = Boat("Yamaha", 45)

    vehicles = [car, boat]

    for vehicle in vehicles:
        vehicle.drive()

import logging
from functools import wraps
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", stream=sys.stdout )

def validate_temperature(setter_method):
    @wraps(setter_method)
    def wrapper(self, value):
        if not (-273.15 <= value <= 1000):
            logging.warning(f"Temperature {value}°C is out of valid range (-273.15°C to 1000°C). Value not changed.")
            return
        return setter_method(self, value)
    return wrapper

class Temperature:
    def __init__(self, celsius: float):
        self._celsius = None
        self.celsius = celsius  # Trigger setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    @validate_temperature
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius_value = (value - 32) * 5/9
        self.celsius = celsius_value  # Validation occurs in celsius setter


if __name__ == "__main__":
    temp = Temperature(25)
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")

    temp.fahrenheit = 212
    print(f"\nAfter setting Fahrenheit to 212°F:")
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")

    temp.celsius = -100
    print(f"\nAfter setting Celsius to -100°C:")
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")

    temp.celsius = -300  # Invalid




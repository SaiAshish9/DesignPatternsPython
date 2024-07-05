from abc import ABC, abstractmethod

class TemperatureProvider(ABC):
    @abstractmethod
    def get_temperature(self):
        pass

class TemperatureSensor:
    def get_temperature_celsius(self):
        return 25  
        
class TemperatureAdapter(TemperatureProvider):
    def __init__(self, sensor):
        self.sensor = sensor

    def get_temperature(self):
        celsius_temperature = self.sensor.get_temperature_celsius()
        fahrenheit_temperature = (celsius_temperature * 9 / 5) + 32
        return fahrenheit_temperature

if __name__ == "__main__":
    sensor = TemperatureSensor()
    adapter = TemperatureAdapter(sensor)
    temperature_fahrenheit = adapter.get_temperature()
    print(f"Temperature in Fahrenheit: {temperature_fahrenheit:.2f}°F")

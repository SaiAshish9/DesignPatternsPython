class Vehicle:

    def __init__(self, builder):
        self.engine = builder.engine
        self.wheel = builder.wheel
        self.airbags = builder.airbags

    def get_engine(self):
        return self.engine

    def get_wheel(self):
        return self.wheel

    def get_airbags(self):
        return self.airbags

    class VehicleBuilder:

        def __init__(self, engine, wheel):
            self.engine = engine
            self.wheel = wheel
            self.airbags = 0  

        def set_airbags(self, airbags):
            self.airbags = airbags
            return self

        def build(self):
            return Vehicle(self)

car = Vehicle.VehicleBuilder("1500cc", 4).set_airbags(4).build()
bike = Vehicle.VehicleBuilder("250cc", 2).build()

print(car.get_engine())
print(car.get_wheel())
print(car.get_airbags())
print(bike.get_engine())
print(bike.get_wheel())
print(bike.get_airbags())

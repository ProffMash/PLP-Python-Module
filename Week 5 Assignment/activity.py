# Base Class
class Vehicle:
    def move(self):
        """Generic move method (to be overridden)"""
        pass

# Subclasses with different move() implementations

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "🚢 Sailing on the water"

class Bicycle(Vehicle):
    def move(self):
        return "🚴 Pedaling on the street"

# Function demonstrating polymorphism
def vehicle_movement(vehicle):
    print(vehicle.move())

# Creating instances
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Output
vehicle_movement(car)
vehicle_movement(plane)
vehicle_movement(boat)
vehicle_movement(bicycle)

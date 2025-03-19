# Our Base Class
class Smartphone:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self._battery_life = battery_life  # Encapsulated attribute

    def display_info(self):
        """Displays smartphone details"""
        return f"{self.brand} {self.model} - ${self.price} | Battery: {self._battery_life}%"

    def charge_battery(self, amount):
        """Charges the battery, but not beyond 100%"""
        self._battery_life = min(100, self._battery_life + amount)
        return f" Battery charged to {self._battery_life}%"

    def make_call(self, number):
        """Simulates making a call"""
        if self._battery_life > 5:
            self._battery_life -= 5
            return f"Calling {number}... Battery now at {self._battery_life}%"
        else:
            return "Low battery! Please charge your phone."

# Derived Class: SmartphonePro
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, price, battery_life, stylus):
        super().__init__(brand, model, price, battery_life)
        self.stylus = stylus  # Extra feature

    def use_stylus(self):
        """Checks if the stylus is available"""
        return "Using the stylus!" if self.stylus else "No stylus available."

# Creating instances
phone1 = Smartphone("Apple", "iPhone 15", 999, 80)
phone2 = SmartphonePro("Samsung", "Galaxy S24 Ultra", 1299, 90, True)

# Output
print(phone1.display_info())
print(phone1.make_call("123-456-7890"))
print(phone1.charge_battery(15))
print()
print(phone2.display_info())
print(phone2.use_stylus())
print(phone2.make_call("987-654-3210"))

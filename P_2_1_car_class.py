# Program 2.1: Define a Car class
class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.is_started = False

  def start(self):
    if not self.is_started:
      self.is_started = True
      print(f"The {self.year} {self.make} {self.model} is starting.")
    else:
      print(f"The {self.year} {self.make} {self.model} is already running.")

  def stop(self):
    if self.is_started:
      self.is_started = False
      print(f"The {self.year} {self.make} {self.model} is stopping.")
    else:
      print(f"The {self.year} {self.make} {self.model} is already stopped.")

# Create a car object and demonstrate methods
print("--- Car Class Demonstration ---")
my_car = Car("Toyota", "Camry", 2022)
print(f'My car: {my_car.make} {my_car.model} ({my_car.year})')
my_car.start()
my_car.stop()
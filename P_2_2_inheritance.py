# Program 2.2: Demonstrate inheritance
# Base Class - Animal
class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    return "Some generic animal sound"
  def move(self):
    return "The animal moves around"

# Derived Class - Cat
class Cat(Animal):
  def speak(self):
    return f"{self.name} says: Meow! Meow!"
  def move(self):
    return f"{self.name} runs quietly."

# Demonstration
my_cat = Cat("Cutie")
animals = [my_cat]
for animal in animals:
  print(animal.speak())
  print(animal.move())
# All classes have a built-in method called __init__(), When create new object __init__ method will execute

# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

# Create a class named Person, use the __init__() method to assign values for name and age:


# When create new object __init_ method will execute
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)




#  We use __init__ because Without the __init__() method, you would need to set properties manually for each object:


# Create a Person class with multiple parameters:
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)


# ------------------------------------------------------------------------------------------------------------------------------------------------

# Self :-
# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.

# Use self to access class properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

# Without self, Python would not know which object's properties you want to access.



# Access multiple properties using self:
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Class Properties  :-
# Properties are variables that belong to a class. They store data for each object created from the class.


# Create a class with properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


# Access the properties of an object:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)


# You can modify the value of properties on objects:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)


# You can delete properties from objects using the del keyword:class Person:
def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error



# -------------------------------------------------------------------------------------------------------------------
# Class attribut vs Object Attribut :--

# Properties defined inside __init__() belong to each object (instance properties):
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:.

# object attribut > class attribute

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# -----------------------------------------------------------------------------------------------------------------------

# You can add new properties to existing objects:
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)
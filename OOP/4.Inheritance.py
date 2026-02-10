# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class :-
# Child class is the class that inherits from another class, also called derived class:-


# Parent   Class

# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# Child Class

# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass


# ----------------------------------------------------------------------------------------------------------------------------------
#  ---------------------------------------------------------------------------------------------------------------------------------

# Add the __init__() Function


# So far we have created a child class that inherits the properties and methods from its parent  class.
# We want to add the __init__() function to the child class (instead of the pass keyword).

# Add the __init__() function to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
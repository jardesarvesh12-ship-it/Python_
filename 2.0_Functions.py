
# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# It helps to avoiding code repetition.


# Why Use Functions?
# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions,
# you would have to write the same calculation code repeatedly:

# Without functions - repetitive code:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# With functions - reusable code:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))



# In Python, a function is defined using the def keyword
def my_function():
  print("Hello from a function")

# To call a function, write its name followed by parentheses:
def my_function():
  print("Hello from a function")
my_function()

# You can call the same function multiple times:
def my_function():
  print("Hello from a function")
my_function()
my_function()
my_function()


# Return Values
# Functions can send data back to the code that called them using the return statement.
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)
 


# Python Function Arguments

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma

def my_function(car_nm):
  print(car_nm + " car")

my_function("Audi")
my_function("BMW")
my_function("Ferari")


# Parameters vs Arguments
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument


# This function expects 2 arguments, and gets 2 arguments::
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")


# You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


# Keyword Arguments
# You can send arguments with the key = value syntax.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
# --> The order matters with positional arguments:



# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)



# Sending a dictionary as an argument:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

# Functions can return values using the return statement:
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


# Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])



# You can specify that a function can have ONLY positional arguments.
# To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

# Without the , / you are actually allowed to use keyword arguments even if the 
# function expects positional arguments:
def my_function(name):
  print("Hello", name)

my_function(name = "Emil")


# Keyword-Only Arguments

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

# Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:
def my_function(name):
  print("Hello", name)

my_function("Emil")




# *args and **kwargs

# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments


# Arbitrary Arguments ----> *args

# DEFINE -->The *args parameter allows a function to accept any number of positional arguments.

# If you do not know how many arguments will be passed into your function, add a ** before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:

# Accessing values from **kwargs:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# 
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


# What is **kwargs?
# The **kwargs parameter allows a function to accept any number of keyword arguments.
# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

# Accessing values from **kwargs:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# Using **kwargs with Regular Arguments
# Regular parameters must come before **kwargs:
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


# You can use both *args and **kwargs in the same function.
# The order must be: 1.regular parameters , 2.*args , 3.**kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.





# Scope:
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope:
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc()

# Global Scope:
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

# A variable created outside of a function is global and can be used by anyone:
x = 300
def myfunc():
  print(x)

myfunc()

print(x)
# The function will print the local x, and then the code will print the global x:
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
# Output --> 200 , 300



# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
def myfunc():
  global x
  x = 300

myfunc()

print(x)


# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())



# Decorators
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.


# Define the decorator first, then apply it with @decorator_name above the function.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


# Using the @changecase decorator on two functions:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# Functions with arguments can also be decorated:

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# One decorator for upper case, and one for adding a greeting:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner
@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())




# Lambda Functions: 
# A lambda function can take any number of arguments, but can only have one expression.

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# We use lambda function
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:



# Generators :--
# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.


def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)


# The send() method allows you to send a value to the generator:
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")


  # The close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()




















































































































# # def sum_cal(a,b):
# #   sum = a+b
# #   print(sum)
# #   return sum

# # sum_cal(2,5)


# # def addition(a,b):
# #   return(a+b)

# # sum= addition(10,57)
# # print(sum)

# def cal_avg(a,b,c):
#     sum = a+b+c
#     avg = sum / 3
#     print(avg)

# cal_avg(2,3,4)


# def cal_avg(addition):
#   return (addition)


def even_odd(num):
  if num % 2 == 0:
    print("number is even:")
  else:
    print("number is odd")

even_odd(5)

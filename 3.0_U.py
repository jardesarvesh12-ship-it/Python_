# Range :
# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

# Creating ranges:-
# range(start, stop, step)


# Call range() With Three Arguments :
# If the range function is called with three arguments, the third argument represents the step value.
# The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.
# range(3, 10, 2) returns a sequence of each number from 3 to 9, with a step of 2:

# Create a range of numbers from 3 to 9:
x = range(3, 10, 2)

# Ranges are often used in for loops to iterate over a sequence of numbers.
for i in range(10):
    print(i)

# Extract a subsequence from a range:
r = range(10)
print(r[2])
print(r[:3])

# Test if the numbers 6 and 7 are present in a range:
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

# ---------------------------------------------------------------------------->

# Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Array methods

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# ----------------------------------------------------------------------------------------->

# iterator :-

# An iterator is an object that contains a countable number of values.meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the 
# methods __iter__() and __next__().

# All these objects have a iter() method which is used to get an iterator:

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.


# Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# ------------------------------------------------------------------------------------------------>

# Module :
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
# created, by using the import statement

# Python Dates :-
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime
x = datetime.datetime.now()
print(x)


# Math Functions :-
# The min() and max() functions can be used to find the lowest or highest value in an iterable:

#minimum and maximim 
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)


# 
import math
x = math.sqrt(64)
print(x)

#  Python JSON
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# Python has a built-in package called json, which can be used to work with JSON data.
import json


# Convert from JSON to Python:
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# --------------------------------------------------------------------------------------->
# Python Regex
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
import re
# ----------------------------------------------------------------------------------------->


# Python PIP
# PIP is a package manager for Python packages, or modules if you like.

# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.



#  Excepction Handling ---->

# try: The try block lets you test a block of code for errors.

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

# The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")



# except: The except block lets you handle the error.
# You can define as many exception blocks as you want
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# else: The else block lets you execute code when there is no error.
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")



# finally : The finally block lets you execute code, regardless of the result of the try- and except blocks.

# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



# As a Python developer you can choose to throw an exception if a condition occurs.

# Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
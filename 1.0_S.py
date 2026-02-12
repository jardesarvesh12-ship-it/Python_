name = input("Enter your name: ")   
print("Welecome: ",name)


numbers = int(input("enter a phone number::"))
print(numbers,"number saved")


float = float(input("enter a float number"))
print(float,"number saved:",type(float))


a,b,c,d = input("enter a number:").split()
print("number 1st is :",a)
print("number 2nd is",b)
print("number 3rd is ",c)
print("number 4th is ",d , type(d))


# If you want to print multiple words on the same line, you can use the end parameter:
print("Hello World!", end=" ")
print("I will print on the same line.")



x, y, z = "Orange", "Banana", "Cherry"
print(x, end=" ")
print(y)
print(z)


# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, type(x))
print(y)
print(z)


a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


b = "Hello, World!"
print(b[2:5])

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# capitalize can Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#  casefold Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


# count Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


# F-strigs But we can combine strings and numbers by using f-strings or the format() method!
age = 36
txt = f"My name is John, I am {age}"
print(txt)


#  Boolen

# You can execute code based on the Boolean answer of a function:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#  Python has two division operators:

# / - Division (returns a float)
# // - Floor division (returns an integer)
x = 12
y = 5

print(x / y)
print(x//y)


# Python allows you to chain comparison operators:
x = 5
print(1 < x < 10)
print(1 < x and x < 10)


# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))

# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print(100 + 5 * 3)

# ----------------------------------------------------------------------------------------------------------------------------->

# LIST

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# The remove() method removes the specified item.
list =["sarvesh",24,8530378249,"kumbhoj","Kolhapur"]
list.remove(24)
print(list)

# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index:
# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# -------------------------------------------------------------------------------------------------------------------------------->

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


#  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

# TUPLE

# Tuple is important because tuple has higher performance higher speed and have good memory management.

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Convert the tuple into a list to be able to change it:
x = ("sarvesh",24,"kolhapur",8530378120)
y = list(x)
print(y, type(y))

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#  Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, 
# (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)




# SET
# in set True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# You cannot access items in a set by referring to an index or a key.
# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# To remove an item in a set, use the remove(), or the discard() method.

# remove ---> If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove "banana" by using the discard() method:
#  If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #You can use the | operator instead of the union() method, and you will get the same result.
print(set3)


# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2) #You can use the & operator instead of the intersection() method, and you will get the same result.
print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) #You can use the - operator instead of the difference() method, and you will get the same result.
print(set3)


# Use the difference_update() method to keep only the items from the first set that are not present in the other set:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2) #You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
print(set1)



# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.

# Use the frozenset() constructor to create a frozenset from any iterable.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


# copy()	     	Returns a shallow copy	
# difference()  	-	Returns a new frozenset with the difference	
# intersection()  	&	Returns a new frozenset with the intersection	
# isdisjoint()  	 	Returns whether two frozensets have an intersection	
# issubset()     	<= / <	Returns True if this frozenset is a (proper) subset of another	
# issuperset()	  >= / >	Returns True if this frozenset is a (proper) superset of another	
# symmetric_difference()  	^	Returns a new frozenset with the symmetric differences	
# union()	         |	Returns a new frozenset containing the union


# -----------------------------------------------------------------------------------

#  Dict

# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]



# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"


# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})



# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# The popitem() method removes the last inserted item 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


# The del keyword removes the item with the specified key name:
# The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)



# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

# Loop through both keys and values, by using the items() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)




# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes 
# made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])


# You can loop through a dictionary by using the items() method like this:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])



# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	      Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	    Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault() 	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
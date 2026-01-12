# name = input("Enter your name: ")   
# print("Welecome: ",name)


# numbers = int(input("enter a phone number::"))
# print(numbers,"number saved")


# float = float(input("enter a float number"))
# print(float,"number saved:",type(float))

# a,b,c,d = input("enter a number:").split()

# print("number 1st is :",a)
# print("number 2nd is",b)
# print("number 3rd is ",c)
# print("number 4th is ",d , type(d))


# # If you want to print multiple words on the same line, you can use the end parameter:
# print("Hello World!", end=" ")
# print("I will print on the same line.")



# x, y, z = "Orange", "Banana", "Cherry"
# print(x, end=" ")
# print(y)
# print(z)

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


# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# F-strigs But we can combine strings and numbers by using f-strings or the format() method!
age = 36
txt = f"My name is John, I am {age}"
print(txt)
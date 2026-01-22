# The if statement evaluates a condition (an expression that results in True or False). If the condition is true, 
# the code block inside the if statement is executed. If the condition is false, the code block is skipped.

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Checking if a number is positive:
number = 15
if number > 0:
  print("The number is positive")



# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true,
#  it executes that block and skips all remaining conditions.

# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of 
# the conditions evaluates to True.

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# 
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")



# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#   
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")


# One-line if statement:
a = 5
b = 2
if a > b: print("a is greater than b")
# One-line if/else that prints a value:
a = 2
b = 330
print("A") if a > b else print("B")
# One line, three outcomes:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# Finding the maximum of two numbers:
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)


# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true


# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# Combining and, or, and not:
age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# User authentication check:
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")


# You can have if statements inside if statements. This is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Checking multiple conditions with nesting:
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


# Three levels of nesting:
score = 85
attendance = 90
submitted = True
if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


# Could also be written with and:
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")


# 
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in
#  the pass statement to avoid getting an error.

a = 33
b = 200
if b > a:
  pass
  
# Why Use pass?
# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later

# Placeholder for future implementation:
age = 16
if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")



#  Match Statment

# The match statement is used to perform different actions based on different conditions.

# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.


# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block


# This is how it works:
# The match expression is evaluated once.
# The value of the expression is compared with the values of each case.
# If there is a match, the associated block of code is executed.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")









#  # While loop

i = 0
while i < 100:
    print(i)
    i += 1

# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#  FOR loop
# A for loop is used for iterating over a sequence
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# Range Function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.
for x in range(6):
  print(x)
# The range() function defaults to 0 as a starting value
for x in range(2, 6):
  print(x) 

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x) 
# Note: The else block will NOT be executed if the loop is stopped by a break statement.


# Nested Loops
# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

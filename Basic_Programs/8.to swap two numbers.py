# to swap two numbers

a = int(input("enter a first number: "))

b = int(input("enter a second number: "))

temp = a
a = b
b = temp

print("After swaping:")
print("A=",a)
print("B=",b)


# Swap Without Using a Third Variable (Pythonic Way)
a1 = int(input("enter a first number: "))

b1 = int(input("enter a second number: "))

a1 , b1 = b1 , a1
print("a1 = ",a1)
print("b1 = ",b1)
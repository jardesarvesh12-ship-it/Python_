
def add(a,b):
    if a > b:
        return a
    else:
        return b
    
num1 = int(input("enter a first number: "))
num2 = int(input("enter a second number: "))

print("greater number is ",add(num1, num2))
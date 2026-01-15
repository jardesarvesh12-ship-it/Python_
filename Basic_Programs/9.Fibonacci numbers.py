number = int(input("enter a number: "))

a,b = 0,1
print("Fibonacci number: ")

for i in range(number):
    print(a,end=" ")
    a,b = b ,a+b



# using function..
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

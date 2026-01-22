def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
    

num = int(input("enter a number : "))
print("number is : ",even_odd(num))
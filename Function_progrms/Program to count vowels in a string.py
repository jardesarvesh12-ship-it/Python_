

def char(text):
    vowles = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowles:
            count += 1
    return count

string = input("enter string: ")

print("volse number in string are: ",char(string))
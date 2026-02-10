
# Almost everything in Python is an object, with its properties and methods.

# Create a Class
# To create a class, use the keyword class

# class is blueprint for creating objects
class Cars:
    names = "BMW"
    color = "Red"
    power = "horse_power"


# Object
s1 = Cars()
print(s1.names)
print(s1.color)



# 
class person:
    name = "sarvesh"
    age = 24
    address = "Kolhapur,kumbhoj"
    occupation = "Master in computer Applictions"
s = person
print(s.name)
print(s.address)



# You can delete objects by using the del keyword:
# del p1


class Polition:
    PM = "Narendr Modi"
    EF = "jayshankar"
    FM = "sudha nirmale"
    CM = "davendre fadanvies"
    xcm = "ajit powar"

p = Polition()
print(p.PM)
print(p.CM)
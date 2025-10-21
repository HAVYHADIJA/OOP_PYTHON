"""Object: Laptop
Class: Computer
Instances:
 A silver Mac, 16GB RAM, 1TB SSD
 Black Dell, 8GB RAM, 512GB SSD"""
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        

"""Object: Dog
Class: Pet
Instances:
 Brown Havy, 1 year
   White Ruby, 6 months
"""        
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""Object: Cake
Class: Pastries
Instances:
1kg Chocolate Cake (Birthday)
20g Strawberry Muffin (Cupcake)
"""
class Cake:
    def __init__(self, flavor, size, occasion):
        self.flavor = flavor
        self.size = size
        self.occasion = occasion


"""Object: Microwave
Class: Electronics
Instances:
Samsung, Silver, 800W, Medium
Black, Small Hisense, 1000W
"""
class Microwave:
    def __init__(self, brand, color, power, size):
        self.brand = brand
        self.color = color
        self.power = power
        self.size = size


"""Object: Shirt
Class: Clothes
Instances:
 Blue collared big silk
 Large white cotton
"""
class Shirt:
    def __init__(self, size, color, material):
        self.size = size
        self.color = color
        self.material = material





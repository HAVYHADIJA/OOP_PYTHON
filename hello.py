print("Hello,OOP World!")

# area of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius * self.radius)

c1 = Circle(5)
c2 = Circle(10)

print("Area:", c1.area())
print("Area:", c2.area())


#function of a phone that calls, take a photo,play music
class Phone:
    def __init__(self, brand, storage):
        self.brand = brand
        self.storage = storage

def call(self, number):
    return f"Calling {number} from {self.brand}"
def take_photo(self):
    return f"Taking a photo with {self.brand} "

def play_music(self, song):
    return f"Playing {song} on {self.brand}"

Phone_1 = Phone("Iphone", "128GB")
Phone_2 = Phone("Samsung","256GB")


print ("Phone brand:" ,Phone_1.brand)
print ("Phone storage", Phone_1.storage)





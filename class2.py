class Gadget:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def start(self):
        print("Gadget started")

class Phone(Gadget):
    def start(self):
        print("Phone is starting")

class Laptop(Gadget):
    def start(self):
        print("Laptop is starting")

gadgets =[Phone(), Laptop()]

for gadget in gadgets:
    gadget.start()


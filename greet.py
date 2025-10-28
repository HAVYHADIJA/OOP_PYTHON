class Precious:
    def greet(self):
        return "Hello from Precious."

class Ben(Precious):
    def greet(self):
        return "Hello from Ben"
    
class Cathy(Precious):
    def greet(self):
        return "Hello from C"

class Danvick(Ben,Cathy):
    pass

d = Danvick()
print(d.greet()) #
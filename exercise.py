
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_mail(self, receiver, message):
        print(f"{self.name} sends: '{message}' to {receiver.name}")
        receiver.receive_mail(self, message)

    def receive_mail(self, sender, message):
        print(f"{self.name} receives mail from {sender.name}: '{message}'")

# Subclasses using inheritance and polymorphism
class Girl(Person):
    def receive_mail(self, sender, message):
        print(f"Girl {self.name} reads reply from {sender.name}: '{message}'")

class Guy(Person):
    def receive_mail(self, sender, message):
        print(f"Guy {self.name} reads mail from {sender.name}: '{message}'")
        reply = f"Hi {sender.name}, nice to hear from you!"
        sender.receive_mail(self, reply)

# Objects
girl = Girl("Sarah", "sarah@mail.com")
guy1 = Guy("Alex", "alex123@mail.com")      #intended guy
guy2 = Guy("Alex", "alex456@mail.com")      #wrong guy

# Story
print("---- STORY ----")
girl.send_mail(guy2, "Hi Alex, I miss you!")   #sent to wrong Alex
print()
guy1.send_mail(girl, "Hey Sarah, how are you?") #real Alex writes later



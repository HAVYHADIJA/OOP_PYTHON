# abstraction.py
# Demonstrates the concept of Abstraction using Abstract Base Classes (ABCs) in Python.

from abc import ABC, abstractmethod

# ==============================================================================
# ABSTRACTION CONCEPTS
# ==============================================================================

"""
Abstraction means:
- Hiding unnecessary details and showing only what is important.
- Hiding the complexity, showing only what the user needs.

In daily life:
When you drive a car, you use the Steering wheel, Pedals, and Dashboard.
You don’t see the complex internal engine code or spark timings (hidden implementation details).

In programming:
You define a simple contract (the Abstract Base Class) that all derived classes must follow,
hiding the specific implementation details of each one.
"""

# ==============================================================================
# EXAMPLE 1: ABSTRACT BASE CLASS (The Contract)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1) The Abstract Base Class (ABC)
# The contract for any object that can be "drawn".
# ------------------------------------------------------------------------------
class Drawable(ABC):
    # This method MUST be implemented by any concrete class inheriting from Drawable.
    # It defines the required interface.
    @abstractmethod
    def draw(self):
        pass

    # A non-abstract method can provide shared behavior.
    def setup_canvas(self):
        print("Canvas setup: Clearing screen...")

# ------------------------------------------------------------------------------
# 2) Concrete Implementations (The Hidden Details)
# ------------------------------------------------------------------------------
class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius
        print(f"Creating circle with radius {radius}")

    # Must implement the abstract method 'draw'
    def draw(self):
        print(f"Drawing a detailed circle on screen (Radius: {self.radius})...")

class Square(Drawable):
    def __init__(self, side):
        self.side = side
        print(f"Creating square with side {side}")

    # Must implement the abstract method 'draw'
    def draw(self):
        print(f"Drawing a complex square on screen (Side: {self.side})...")


print("\n--- Example 1: Basic Drawable ABC ---")
circle = Circle(5)
square = Square(10)

# The user only interacts with the 'draw' method, not the shape's complex calculations.
print("\nCalling draw():")
circle.setup_canvas()
circle.draw()

square.setup_canvas()
square.draw()


# Attempting to instantiate the abstract class will raise an error (Abstraction enforced)
# try:
#     abstract_object = Drawable()
# except TypeError as e:
#     print(f"\nCaught Expected Error: {e}")


# ==============================================================================
# EXAMPLE 2: NOTIFICATION SYSTEM (Hiding Delivery Method)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1) The Abstract Alert Contract
# Defines that all alerts must have a 'notify' method.
# ------------------------------------------------------------------------------
class Alert(ABC):
    @abstractmethod
    def notify(self, title, message):
        # pass is the standard placeholder for abstract methods
        pass

# ------------------------------------------------------------------------------
# 2) Concrete Implementations
# Each implementation handles the complex, hidden process of sending the alert.
# The user only needs to call 'notify()'.
# ------------------------------------------------------------------------------
class EmailAlert(Alert):
    def notify(self, title, message):
        # Complex steps for connecting to SMTP server, formatting email, etc. are hidden.
        print(f"EMAIL: {title} - {message}")

class SMSAlert(Alert):
    def notify(self, title, message):
        # Complex steps for API calls to a cellular provider are hidden.
        print(f"SMS: {title} - {message}")

class AppAlert(Alert):
    def notify(self, title, message):
        # Complex steps for sending push notifications via Google/Apple are hidden.
        print(f"APP: {title} - {message}")


print("\n--- Example 2: Polymorphic Alert System ---")
alerts = [EmailAlert(), SMSAlert(), AppAlert()]
event_title = "Warning"
event_message = "Battery low"

# Polymorphism via Abstraction: the same call 'a.notify' works for different types,
# but the underlying delivery mechanism is completely hidden from the user.
for a in alerts:
    a.notify(event_title, event_message)


# inheritance.py
# Examples demonstrating inheritance, method overriding, and using super() in Python.

SECTION_BREAK = "\n" + "="*50 + "\n"


# ==============================================================================
# Example 1: Basic Inheritance (Child inherits parent's methods/attributes)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 1: BASIC INHERITANCE")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    # Method inherited by all children
    def move(self):
        print(f"{self.brand} moves!")

class Car(Vehicle):
    # Car inherits __init__ and move()
    def drive(self):
        print(f"{self.brand} is driving fast.")

class Bicycle(Vehicle):
    # Bicycle inherits __init__ and move()
    def pedal(self):
        print(f"{self.brand} is being pedalled.")

# Usage
c = Car("Toyota")
b = Bicycle("Raleigh")

c.move()    # Inherited from Vehicle
c.drive()   # Car's own method
b.move()    # Inherited from Vehicle
b.pedal()   # Bicycle's own method


# ==============================================================================
# Example 2: Method Overriding (Child changes parent's behavior)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 2: METHOD OVERRIDING")

class Dog:
    def speak(self):
        print("Woof")
        
    def description(self):
        print("A generic dog.")

class GoldenRetriever(Dog):
    # Overrides the parent's speak method
    def speak(self):
        print("Gentle Bark!")
    
    # Inherits description() as is

# Usage
dog = Dog()
retriever = GoldenRetriever()

dog.speak()        # Calls Dog.speak()
retriever.speak()  # Calls GoldenRetriever.speak() (Overridden)
retriever.description() # Calls Dog.description() (Inherited)


# ==============================================================================
# Example 3: Using super() in __init__ (Calling the Parent's Constructor)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 3: USING super() IN __init__")

class Parent:
    def __init__(self, a):
        self.a = a
        print("Parent init called.")

class Child(Parent):
    def __init__(self, a, b):
        # Call the parent's constructor first to initialize attribute 'a'
        super().__init__(a)
        
        # Then initialize the child's unique attribute 'b'
        self.b = b
        print("Child init called.")

# Usage
child = Child(10, 20)
print(f"Child has attributes: a={child.a}, b={child.b}")


# ==============================================================================
# Example 4: super() for Methods (Extending Parent's functionality)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 4: USING super() FOR METHODS")

class Shape:
    def info(self):
        print("I am a 2D shape.")

class Rectangle(Shape):
    def info(self):
        # Call the parent's info method
        super().info()
        # Add custom, specific info
        print("I have four right angles.")

# Usage
r = Rectangle()
r.info()


# ==============================================================================
# Example 5: Hierarchy Inheritance (Political Parties)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 5: HIERARCHY INHERITANCE")

class PoliticalParty:
    # Shared Class Attribute
    party_name = "Independent"

    # Shared Method (Default Slogan)
    def slogan(self):
        print("Vote for change!") # Generic slogan

    def __init__(self, candidate_name):
        self.candidate_name = candidate_name

    def info(self):
        print("Candidate: " + self.candidate_name)
        print("Party: " + self.party_name)
        self.slogan()

# Child Class 1: Overrides party_name and slogan()
class LibertyCandidate(PoliticalParty):
    party_name = "Liberty"
    def slogan(self):
        print("Freedom and prosperity for all!")

# Child Class 2: Overrides only party_name, inherits default slogan()
class UnityCandidate(PoliticalParty):
    party_name = "Unity"

# Child Class 3: Overrides party_name and slogan()
class GreenCandidate(PoliticalParty):
    party_name = "Green"
    def slogan(self):
        print("Protecting the planet for future generations!")

# Usage
cand1 = LibertyCandidate("Amina K.")
cand2 = UnityCandidate("Brian T.")
cand3 = GreenCandidate("Carol M.")

print("\n--- Liberty Candidate (Custom Slogan) ---")
cand1.info()

print("\n--- Unity Candidate (Default Slogan) ---")
cand2.info() # Uses PoliticalParty.slogan()

print("\n--- Green Candidate (Custom Slogan) ---")
cand3.info()

# last_oop_review.py
# Final review and practice session covering Inheritance, Abstraction, Encapsulation,
# Polymorphism, and Operator Overloading.

from abc import ABC, abstractmethod
import math

SECTION_BREAK = "\n" + "=" * 80 + "\n"

# ==============================================================================
# Q1: GYM MEMBER CLASS (Basic OOP)
# A small gym wants to store details of its members.
# - Stores name, age, membership_type in the constructor.
# - Has a method show_info() that prints the member details.
# ==============================================================================

print(SECTION_BREAK)
print("Q1: GYM MEMBER CLASS")

class Member:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type

    def show_info(self):
        print(f"Member Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Membership Type: {self.membership_type}")
        print("-" * 32)

# Create two Member objects and call show_info() on each.
member1 = Member("Alice", 22, "Monthly")
member2 = Member("Brian", 30, "Yearly")

member1.show_info()
member2.show_info()


# ==============================================================================
# Q2: AIRLINE BOOKING SYSTEM (Abstraction, Inheritance, Overloading, Polymorphism)
# ==============================================================================

print(SECTION_BREAK)
print("Q2: AIRLINE BOOKING SYSTEM (Abstract Class, Inheritance, Overloading)")

# Abstract Class: Ticket (The Contract)
class Ticket(ABC):
    LUGGAGE_FEE_PER_KG = 5.0 # Constant for luggage calculation

    def __init__(self, passenger_name: str, base_fare: float):
        self.passenger_name = passenger_name
        self.base_fare = base_fare
        self.fees = 0.0

    @abstractmethod
    def total_price(self) -> float:
        """Abstract method to calculate the final price including class fees."""
        # Must be implemented by all subclasses.
        pass
    
    # Operator Overloading: Defines what happens when you use the '+' operator
    # between a Ticket object (self) and another object (Luggage in this case).
    def __add__(self, other):
        if isinstance(other, Luggage):
            luggage_cost = other.get_weight() * self.LUGGAGE_FEE_PER_KG
            # Return the new total price
            return self.total_price() + luggage_cost
        raise TypeError("Unsupported operand type for +: Ticket and " + str(type(other)))

    def show_details(self):
        print(f"  Passenger: {self.passenger_name}")
        print(f"  Base Fare: ${self.base_fare:.2f}")
        print(f"  Class Fees: ${self.fees:.2f}")
        print(f"  Total Ticket Price: ${self.total_price():.2f}")


# Subclasses: Implement the abstract method total_price()

class EconomyTicket(Ticket):
    def __init__(self, passenger_name: str, base_fare: float):
        super().__init__(passenger_name, base_fare)
        self.fees = 10.0  # Small fee

    def total_price(self) -> float:
        return self.base_fare + self.fees

class BusinessTicket(Ticket):
    def __init__(self, passenger_name: str, base_fare: float):
        super().__init__(passenger_name, base_fare)
        self.fees = 150.0 # High fee for amenities

    def total_price(self) -> float:
        return self.base_fare + self.fees

class FirstClassTicket(Ticket):
    def __init__(self, passenger_name: str, base_fare: float):
        super().__init__(passenger_name, base_fare)
        self.fees = 400.0 # Highest fee

    def total_price(self) -> float:
        return self.base_fare + self.fees


# Class Luggage: Contains a private weight attribute (__weight)
class Luggage:
    def __init__(self, weight_kg: float):
        # Pseudo-private attribute
        self.__weight = weight_kg 

    def get_weight(self):
        # Controlled access to the private attribute
        return self.__weight


# Class AirportTax (Duck Typing/Polymorphism Example)
class AirportTax:
    TAX_RATE = 0.15 # 15% Tax

    def apply(self, ticket):
        # Duck Typing: We don't care about the type, just that it has the total_price method.
        # This will work for EconomyTicket, BusinessTicket, or any other class
        # that defines total_price().
        
        try:
            current_total = ticket.total_price()
            tax_amount = current_total * self.TAX_RATE
            
            print(f"\n--- Applying Airport Tax ({self.TAX_RATE * 100:.0f}%) ---")
            print(f"  Subtotal: ${current_total:.2f}")
            print(f"  Tax Amount: ${tax_amount:.2f}")
            print(f"  Final Price (with tax): ${current_total + tax_amount:.2f}")
            print("-" * 32)
            return current_total + tax_amount
        except AttributeError:
            print(f"Error: Object {type(ticket).__name__} does not have a total_price() method (Duck Typing failed).")
            return 0.0


# --- DEMONSTRATION ---

# 1. Create objects
e_ticket = EconomyTicket("Alice Smith", 450.00)
b_ticket = BusinessTicket("Ben Clark", 800.00)
luggage = Luggage(15.0) # 15 kg

# 2. Polymorphism (Display details for all ticket types)
print("\n--- TICKET DETAILS (Polymorphism) ---")
for t in [e_ticket, b_ticket]:
    print(f"\n{type(t).__name__}:")
    t.show_details()

# 3. Operator Overloading (Ticket + Luggage)
luggage_total = e_ticket + luggage
print(f"\n--- OPERATOR OVERLOADING (Ticket + Luggage) ---")
print(f"  Economy Ticket Price: ${e_ticket.total_price():.2f}")
print(f"  Luggage Cost (15kg * ${Ticket.LUGGAGE_FEE_PER_KG:.2f}): ${15 * Ticket.LUGGAGE_FEE_PER_KG:.2f}")
print(f"  Total Price with Luggage: ${luggage_total:.2f}")

# 4. Duck Typing (Airport Tax)
tax_service = AirportTax()
tax_service.apply(b_ticket) # Applies tax to BusinessTicket

# polymorphism.py
# Examples demonstrating Polymorphism through Method Overriding and Duck Typing.

SECTION_BREAK = "\n" + "=" * 60 + "\n"

# ==============================================================================
# 1) Polymorphism via Method Overriding (Requires Inheritance)
# ==============================================================================

print(SECTION_BREAK)
print("1) METHOD OVERRIDING (INHERITANCE)")

class Animal:
    """The Base/Parent Class."""
    def speak(self):
        # Default behavior
        print("I am an animal and I make a sound.")

class Dog(Animal):
    """Child Class 1: Overrides speak()"""
    def speak(self):
        # New, specific behavior
        print("Woof woof!")

class Cat(Animal):
    """Child Class 2: Overrides speak()"""
    def speak(self):
        # New, specific behavior
        print("Meow!")

class Duck(Animal):
    """Child Class 3: Overrides speak()"""
    def speak(self):
        # New, specific behavior
        print("Quack!")

# Create a list of different objects
animals = [Dog(), Cat(), Duck()]

print("\nCalling the same method (speak()) on different objects:")
# Loop over the list and call the same method name.
# Polymorphism allows each object to execute its own unique version of the method.
for animal in animals:
    animal.speak()


# ==============================================================================
# 2) Polymorphism via Duck Typing (No Inheritance Required)
# ==============================================================================

print(SECTION_BREAK)
print("2) DUCK TYPING (NO INHERITANCE)")
# The principle: "If it walks like a duck and it quacks like a duck, then it is a duck."
# In Python: If an object has the required method (e.g., 'draw'), we can call it.

class RectDrawer: # No parent class
    def draw(self): # Same method name
        print("Draw rectangle (Width 10, Height 5)") # Specific implementation

class CircleDrawer: # No parent class
    def draw(self): # Same method name
        print("Draw circle (Radius 5)") # Specific implementation

class TextTool: # No parent class
    def draw(self): # Same method name
        print("Draw text: 'Hello World'") # Specific implementation

# One list of diverse objects
canvas = [RectDrawer(), CircleDrawer(), TextTool()]

print("\nCalling the same method (draw()) via Duck Typing:")
# The loop doesn't care about the object's type (class name), only that it has a 'draw()' method.
for shape in canvas:
    shape.draw() # Duck typing call
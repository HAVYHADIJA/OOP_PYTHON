# week_1_oop_intro.py

import math
from dataclasses import dataclass

SECTION_BREAK = "\n" + "="*60 + "\n"

# ==============================================================================
# 1) Procedural Programming Example — Circle Area
# ==============================================================================

def area_of_circle_procedural(radius):
    """Procedural: compute area using a function + primitive data."""
    return math.pi * radius * radius

# Demo
r1 = 5
area = area_of_circle_procedural(r1)
print(SECTION_BREAK)
print("1) PROCEDURAL PROGRAMMING EXAMPLE")
print(f"Radius = {r1}, Area = {area:.2f}")


# ==============================================================================
# 2) OOP — BankAccount Example
# ==============================================================================

class BankAccount:
    """Simple OOP example: state (balance) + behavior (deposit/withdraw)."""
    def __init__(self, balance=0.0):
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance = {self.balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance = {self.balance:.2f}")

# Demo
print(SECTION_BREAK)
print("2) OOP – BANK ACCOUNT EXAMPLE")
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Final balance: {account.balance:.2f}")


# ==============================================================================
# 3) First Class in Python — Student
# ==============================================================================

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Demo
print(SECTION_BREAK)
print("3) FIRST CLASS IN PYTHON – STUDENT")
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
print(s1.introduce())
print(s2.introduce())


# ==============================================================================
# 4) Real-Life Analogy — Phone
# ==============================================================================

class Phone:
    def __init__(self, brand: str, storage: str):
        self.brand = brand
        self.storage = storage

    def call(self, number: str):
        print(f"Calling {number} from {self.brand} phone...")

    def take_photo(self):
        print(f"*Click!* {self.brand} took a photo. (Storage left: {self.storage})")

# Demo
print(SECTION_BREAK)
print("4) REAL-LIFE ANALOGY – PHONE")
my_phone = Phone("Samsung", "128GB")
my_phone.call("123-456-789")
my_phone.take_photo()


# ==============================================================================
# 5) Mini Game — Player.attack()
# ==============================================================================

class Player:
    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health

    def attack(self, other: "Player", damage: int = 10):
        other.health = max(0, other.health - damage)
        print(f"{self.name} attacks {other.name}! {other.name}'s health = {other.health}")

    def heal(self, amount: int = 5):
        self.health += amount
        print(f"{self.name} heals by {amount}. Health = {self.health}")

# Demo
print(SECTION_BREAK)
print("5) MINI GAME – PLAYER ATTACK")
p1 = Player("Knight")
p2 = Player("Dragon")
p1.attack(p2)     # Knight attacks Dragon
p2.attack(p1, 15) # Dragon attacks harder
p1.heal()         # Knight heals


# ==============================================================================
# 6) Challenge — Car dataclass
# ==============================================================================

@dataclass
class Car:
    brand: str
    year: int

    def honk(self):
        print("Beep! Beep!")

# Demo
print(SECTION_BREAK)
print("6) CHALLENGE – CAR")
c1 = Car("Toyota", 2018)
c2 = Car("Honda", 2021)
print(f"Car 1: {c1.brand} ({c1.year})")
print(f"Car 2: {c2.brand} ({c2.year})")
c1.honk()
c2.honk()


# ==============================================================================
# 7) Extra — Encapsulation & Properties (Temperature)
# ==============================================================================

class Temperature:
    """Encapsulation using @property to control attribute access."""
    def __init__(self, celsius: float = 0.0):
        self._celsius = celsius  # use underscore to indicate 'internal'

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32

# Demo
print(SECTION_BREAK)
print("7) EXTRA – ENCAPSULATION & PROPERTIES")
t = Temperature(25)
print(f"Temp: {t.celsius}°C / {t.fahrenheit}°F")
t.celsius = 30
print(f"Updated: {t.celsius}°C / {t.fahrenheit}°F")
try:
    t.celsius = -300
except ValueError as e:
    print("Error:", e)


# ==============================================================================
# 8) Extra — Inheritance & Polymorphism (Animal, Dog, Cat)
# ==============================================================================

class Animal:
    def speak(self) -> str:
        # This is an abstract method - forces children to implement it
        raise NotImplementedError("Subclasses must implement abstract method speak")

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

def make_it_speak(creature: Animal):
    # Polymorphism: we don't care which Animal subtype it is.
    print(creature.speak())

# Demo
print(SECTION_BREAK)
print("8) EXTRA – INHERITANCE & POLYMORPHISM")
dog = Dog()
cat = Cat()
make_it_speak(dog)
make_it_speak(cat)


# ==============================================================================
# 9) Extra — Exception Handling (divide)
# ==============================================================================

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Both a and b must be numbers!")
        return None
    finally:
        # finally always executes
        pass

# Demo
print(SECTION_BREAK)
print("9) EXTRA – EXCEPTION HANDLING")
print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))
print("10 / 'x' =", divide(10, 'x'))


# week_v_oop_advanced.py
# Instructor: Mr. Simon Lubambo
# Department: Computing & Technology

# This script contains runnable examples for Interfaces, Multiple Inheritance,
# Method Resolution Order (MRO), and Exception Handling in Python.

import logging
import inspect # Used to demonstrate MRO

# Configuration for logging (used in sections 8 and 9)
# Creates 'errors.log' and 'mini_errors.log' files in the same directory.
logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(message)s'
)

SECTION_BREAK = "\n" + "="*60 + "\n"


# ==============================================================================
# 0) Quick Warm-Up Recap — Inheritance & Polymorphism
# ==============================================================================

print(SECTION_BREAK)
print("0) QUICK WARM-UP RECAP: Inheritance & Polymorphism")

class Student:
    def greet(self):
        print("👋 I'm a student.")

class ClassRep(Student):
    def greet(self):
        # Method Overriding: replaces parent's greet()
        print("🗣️ I'm the Class Rep, taking attendance!")

class GuildPresident(Student):
    def greet(self):
        # Method Overriding: new behavior
        print("🎤 I'm the Guild President — let's improve campus!")

people = [Student(), ClassRep(), GuildPresident()]
for p in people:
    p.greet()
# Polymorphism: same call (p.greet()) -> different outputs based on the object type.


# ==============================================================================
# 1) Interfaces vs Abstract Classes (Python Style)
# ==============================================================================

print(SECTION_BREAK)
print("1) INTERFACES VS ABSTRACT CLASSES")

# "Interface-like" base classes (define contracts/capabilities)
class MeetingAttendee:
    def attend_meeting(self):
        print("🪑 Attending a generic meeting...")

class BudgetApprover:
    def approve_budget(self):
        print("💰 Approving a generic budget...")

# "Abstract-like" base class with shared code (common behavior)
class CampusLeader:
    def intro(self):
        # Shared method: reusable code for all leaders
        print("🎓 I am a campus leader.")

# Concrete classes combine contracts and shared code via Multiple Inheritance
class Dean(CampusLeader, MeetingAttendee, BudgetApprover):
    def attend_meeting(self):
        # Override specific behavior
        print("🎓 Dean chairs the faculty meeting.")
    # inherits approve_budget() and intro()

class GuildPresident(CampusLeader, MeetingAttendee, BudgetApprover):
    def attend_meeting(self):
        # Override specific behavior
        print("🎤 Guild President meets with the student council.")
    def approve_budget(self):
        # Override custom behavior
        print("🧾 Guild President reviews and signs club proposals.")

leader1 = Dean()
leader1.intro()
leader1.attend_meeting()
leader1.approve_budget()

leader2 = GuildPresident()
leader2.intro()
leader2.attend_meeting()
leader2.approve_budget()


# ==============================================================================
# 2) Python’s Multiple Inheritance
# ==============================================================================

print(SECTION_BREAK)
print("2) PYTHON'S MULTIPLE INHERITANCE")

# Multiple inheritance = combine independent capabilities
class Athlete:
    def train(self):
        print("🏃 Training every morning.")

class Scholar:
    def study(self):
        print("📚 Studying for exams.")

class StudentAthlete(Athlete, Scholar):  # Inherits from Athlete AND Scholar
    def balance(self):
        print("⚖️ Balancing sports and academics!")

sa = StudentAthlete()
sa.train()  # from Athlete
sa.study()  # from Scholar
sa.balance() # its own method


# ==============================================================================
# 3) MRO — Method Resolution Order (The Diamond Problem Solution)
# ==============================================================================

print(SECTION_BREAK)
print("3) MRO — METHOD RESOLUTION ORDER")

class A:
    def shout(self): print("A shouts")

class B(A):
    def shout(self): print("B shouts")

class C(A):
    # C does not override shout() in the original notebook, using A's shout() if needed.
    pass 

class D(B, C):  # left parent is B, right parent is C
    pass

d = D()
d.shout() # -> "B shouts" because B is the first parent checked (left-to-right rule).

# Print the MRO path explicitly
print("MRO:", inspect.getmro(D))


# ==============================================================================
# 4) Java-Style Interfaces (Contrast) and Python Equivalent
# ==============================================================================

print(SECTION_BREAK)
print("4) PYTHON EQUIVALENT TO JAVA INTERFACE")

# PYTHON EQUIVALENT (Drivable is the interface contract)
class Drivable:
    def drive(self):
        print("Driving (generic)")

class Car(Drivable):
    def drive(self):
        # Subclass fulfills the contract by overriding
        print("🚗 Car drives on the road.")

c = Car()
c.drive()


# ==============================================================================
# 5) try / except / finally — Basic Error Handling
# ==============================================================================

print(SECTION_BREAK)
print("5) TRY / EXCEPT / FINALLY")

print("Start")
try:
    x = 10 / 0 # risky: ZeroDivisionError
    print("This won't run")
except ZeroDivisionError: # catch the specific error
    print("❌ You can't divide by zero.")
finally:
    # finally always executes, regardless of error
    print("✅ Finally: clean up (e.g., close files, release resources).")
print("End")


# ==============================================================================
# 6) Built-In Exceptions — Common Cases
# ==============================================================================

print(SECTION_BREAK)
print("6) BUILT-IN EXCEPTIONS")

data = {"name": "Anna"}
items = [1, 2, 3]

try:
    print(items[10])
except IndexError:
    print("📏 IndexError: that list position doesn't exist.")

try:
    print(data["age"])
except KeyError:
    print("🔑 KeyError: 'age' is missing in the data.")

try:
    int("not-a-number")
except ValueError:
    print("🔢 ValueError: cannot convert to integer.")

try:
    result = "3" + 2
except TypeError:
    print("🔧 TypeError: you mixed data types incorrectly.")


# ==============================================================================
# 7) Custom Exceptions — Define Your Own Rules
# ==============================================================================

print(SECTION_BREAK)
print("7) CUSTOM EXCEPTIONS")

class LateSubmissionError(Exception):
    # Custom exception classes usually need no content (pass)
    pass

def submit_assignment(on_time):
    if not on_time:
        # raise: throw an error intentionally to signal a rule violation
        raise LateSubmissionError("🚨 Assignment submitted after the deadline!")
    print("✅ Assignment received on time.")

# use it
try:
    submit_assignment(False) # simulate late
except LateSubmissionError as e: # catch your custom error
    print("Handled:", e)


# ==============================================================================
# 8) Error Logging — Record Problems Instead of Printing
# ==============================================================================

print(SECTION_BREAK)
print("8) ERROR LOGGING")

def risky_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # exc_info=True -> include stack trace in the log file ('errors.log')
        logging.error("Division by zero in risky_divide(%s, %s)", a, b, exc_info=True)
        print("❌ Can't divide by zero. Error has been logged.")
        return None
    finally:
        pass

r1 = risky_divide(10, 2)   # OK
r2 = risky_divide(10, 0)   # logs error to errors.log
print("Results:", r1, r2)


# ==============================================================================
# 9) Mini Practice — Interfaces + MI + Exceptions + Logging
# ==============================================================================

print(SECTION_BREAK)
print("9) MINI PRACTICE")

# Reconfigure logging for the mini practice to a different file
logging.basicConfig(filename='mini_errors.log', level=logging.ERROR)

# "interface-like" capabilities
class Readable:
    def read_content(self):
        print("📖 Reading content...")

class Writable:
    def write_content(self, text):
        print(f"✍️ Writing: {text}")

# custom error
class DiskFullError(Exception):
    pass

class Notebook(Readable, Writable): # Multiple inheritance
    def save(self, text):
        # Rule: if text is too long, raise custom error
        if len(text) > 20:
            raise DiskFullError("💽 Disk is full. Can't save more text.")
        print("💾 Saved successfully!")

nb = Notebook()

try:
    nb.read_content()
    nb.write_content("Short note")
    nb.save("Short note")                # OK
    nb.save("This line is way too long to fit...") # triggers custom error
except DiskFullError as e:
    logging.error("Save failed", exc_info=True)  # log error with stack trace
    print("❌ Save failed:", e)
finally:
    print("✅ Done (finally).")

print(SECTION_BREAK)

# car_examples.py
# Examples demonstrating Python Classes, Constructors, and Encapsulation

SECTION_BREAK = "\n" + "=" * 60 + "\n"

# ==============================================================================
# Example 1: Basic Class Structure and Constructor (__init__)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 1: BASIC CLASS AND CONSTRUCTOR")

class Car_Ex1:
    # The __init__ method is automatically called when you create a new object
    def __init__(self, speed, color):
        print(f"Initializing Car: Speed={speed}, Color={color}")

        # Store the values inside the object (attributes)
        self.speed = speed
        self.color = color

        print("the __init__ is called")


# Creating objects (instances) of the Car class
ford = Car_Ex1(200, 'gray')
honda = Car_Ex1(250, 'blue')
audi = Car_Ex1(300, 'black')

# Accessing the attributes of the ford object
print("\nAccessing ford attributes:")
print(f"Speed: {ford.speed}")
print(f"Color: {ford.color}")


# ==============================================================================
# Example 2: Modifying an Attribute Directly (Lack of Encapsulation)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 2: MODIFYING ATTRIBUTES DIRECTLY")

class Car_Ex2:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        print("the __init__ is called")

# Creating objects
ford_ex2 = Car_Ex2(200, 'red')
honda_ex2 = Car_Ex2(250, 'blue')
audi_ex2 = Car_Ex2(300, 'black')

# Changing the attribute directly (This is simple, but risky if you need validation)
ford_ex2.speed = 300

# Accessing the modified attributes
print("\nAccessing ford_ex2 attributes (after modification):")
print(f"Speed: {ford_ex2.speed}")
print(f"Color: {ford_ex2.color}")


# ==============================================================================
# Example 3: Using Getter/Setter Methods for Control (Basic Encapsulation)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 3: USING GETTER/SETTER METHODS")

class Car_Ex3:
    def __init__(self, speed, color):
        # Store the values inside the object
        self.speed = speed
        self.color = color

    # Setter Method (Controls how speed is changed)
    def set_speed(self, value):
        # Could add validation here (e.g., if value < 0: raise ValueError)
        self.speed = value
    
    # Getter Method (Controls how speed is read)
    def get_speed(self):
        return self.speed


# Creating objects
ford_ex3 = Car_Ex3(200, 'red')
honda_ex3 = Car_Ex3(250, 'blue')
audi_ex3 = Car_Ex3(300, 'black')

# Use the setter method
ford_ex3.set_speed(500)

# Direct assignment still works in this implementation, overriding the set_speed() call
ford_ex3.speed = 400

# Accessing the attributes
print("\nAccessing ford_ex3 attributes:")
print(f"Speed (via getter, reflecting direct change): {ford_ex3.get_speed()}")
print(f"Color: {ford_ex3.color}")


# ==============================================================================
# Example 4: Pseudo-Private Attributes (Name Mangling)
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 4: PSEUDO-PRIVATE ATTRIBUTES (NAME MANGLING)")

class Hello:
    def __init__(self, name):
        self.a = 10      # Public
        self._b = 20     # Protected (convention only)
        self.__c = 30    # Pseudo-Private (name mangled)

hello = Hello("name")
print(f"Public attribute 'a': {hello.a}")
print(f"Protected attribute '_b': {hello._b}")

# Accessing the '__c' attribute directly fails due to name mangling
try:
    print(hello.__c) 
except AttributeError as e:
    print(f"\nCaught Expected Error: {e}")
    print("Error occurs because __c is pseudo-private and accessed directly.")


# ==============================================================================
# Example 5: Full Encapsulation with Pseudo-Private Attributes and Accessors
# ==============================================================================

print(SECTION_BREAK)
print("EXAMPLE 5: FULL ENCAPSULATION WITH GETTERS/SETTERS")

class Car_Ex5:
    def __init__(self, speed, color):
        # Attributes are made pseudo-private using double underscores (__)
        self.__speed = speed
        self.__color = color
        
    # Setter Method (Mutator)
    def set_speed(self, value):
        self.__speed = value
        
    # Getter Method (Accessor)
    def get_speed(self):
        return self.__speed
    
    # Setter for color
    def set_color(self, value):
        self.__color = value
        
    # Getter for color
    def get_color(self):
        return self.__color


# Creating objects
ford_ex5 = Car_Ex5(200, 'red')
# honda_ex5 = Car_Ex5(250, 'blue') # Not used, but demonstrating creation
# audi_ex5 = Car_Ex5(300, 'black') # Not used

# Use setter methods
ford_ex5.set_speed(500)
ford_ex5.set_color("yellow")

# Note: The line 'ford_ex5.__speed = 400' in the notebook *creates a new, public attribute*
# named __speed on the instance, but it does NOT change the internal __speed attribute.

# Accessing the attributes via getter methods
print("\nAccessing ford_ex5 attributes:")
print(f"Speed (via getter): {ford_ex5.get_speed()}")
print(f"Color (via getter): {ford_ex5.get_color()}")

# Trying to access the attribute directly fails because __color is pseudo-private
try:
    print(ford_ex5.color)
except AttributeError as e:
    print(f"\nCaught Expected Error: {e}")
    print("Error occurs because 'color' (without __) does not exist.")
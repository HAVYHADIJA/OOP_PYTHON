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

# encapsulation_examples.py
# Demonstrates visibility, classic getters/setters, validation, and read-only attributes.

from datetime import datetime

SECTION = "\n" + "=" * 72 + "\n"

# ==============================================================================
# 0) VISIBILITY: public / _protected / __private
# ==============================================================================

class VisibilityDemo:
    def __init__(self):
        # Public: everyone can read/write directly.
        self.public_attr = "PUBLIC"
        
        # Protected (by convention): convention suggests 'internal use only'.
        self._protected_attr = "PROTECTED (convention)"
        
        # Pseudo-Private: name-mangled by Python (harder to access accidentally).
        self.__private_attr = "PRIVATE (name-mangled)"

    def reveal_private(self):
        # The proper way: access private attributes INSIDE the class method.
        return self.__private_attr


# DEMO: what you can access from outside
print(SECTION + "0) VISIBILITY: public / _protected / __private")
v = VisibilityDemo()

# Public access:
print("Public:", v.public_attr)

# Protected access (allowed, but discouraged by convention):
print("Protected (by convention):", v._protected_attr)

# Private access via method (proper way):
print("Private via method:", v.reveal_private())

# Private access via name-mangling (discouraged, but possible):
print("Private via name-mangling:", v._VisibilityDemo__private_attr)


# ==============================================================================
# 1) CLASSIC GETTERS/SETTERS (no @property)
# ==============================================================================

print(SECTION + "1) GETTERS/SETTERS (no @property)")

class CourseClassic:
    def __init__(self, name: str):
        # Use _ convention for internal storage.
        self._name = name

    def get_name(self) -> str:
        # Getter: Safe read.
        return self._name

    def set_name(self, new_name: str) -> None:
        # Setter: Safe write with validation.
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = new_name.strip()


c = CourseClassic("OOP")
print("get_name:", c.get_name())
c.set_name("Encapsulation")
print("after set_name:", c.get_name())


# ==============================================================================
# 2) STUDENT — GPA WITH VALIDATION
# ==============================================================================

print(SECTION + "2) STUDENT GPA (classic getters/setters)")

class Student:
    def __init__(self, name: str, gpa: float = 0.0):
        self.name = name
        self._gpa = 0.0          # internal storage
        self.set_gpa(gpa)        # Use the setter even in __init__ for validation

    def get_gpa(self) -> float:
        return self._gpa

    def set_gpa(self, value: float) -> None:
        v = float(value)
        # Validation rule: GPA must be between 0.0 and 5.0
        if not (0.0 <= v <= 5.0):
            raise ValueError("GPA must be between 0.0 and 5.0")
        self._gpa = v

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, GPA: {self.get_gpa():.2f}"


s = Student("Aisha", 4.4)
print(s.introduce())
try:
    s.set_gpa(6.7)    # Test the validation
except ValueError as e:
    print("Invalid GPA blocked:", e)


# ==============================================================================
# 3) TEMPERATURE — read-only computed values
# ==============================================================================

print(SECTION + "3) TEMPERATURE (computed read-only)")

class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._celsius = 0.0
        self.set_celsius(celsius)

    def set_celsius(self, value: float) -> None:
        v = float(value)
        # Validation rule: cannot go below absolute zero
        if v < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = v

    def get_celsius(self) -> float:
        return self._celsius

    def get_fahrenheit(self) -> float:
        # Computed attribute (read-only)
        return (self._celsius * 9.0 / 5.0) + 32.0

    def get_kelvin(self) -> float:
        # Computed attribute (read-only)
        return self._celsius + 273.15


t = Temperature(25)
print("C:", t.get_celsius(), "F:", round(t.get_fahrenheit(), 2), "K:", round(t.get_kelvin(), 2))
try:
    t.set_celsius(-500)  # Test the validation
except ValueError as e:
    print("Invalid celsius blocked:", e)


# ==============================================================================
# 4) BANK ACCOUNT — encapsulated balance
# ==============================================================================

print(SECTION + "4) BANK ACCOUNT (safe updates only)")

class BankAccount:
    def __init__(self, balance: float = 0.0):
        self._balance = float(balance)

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        a = float(amount)
        if a <= 0.0:
            raise ValueError("Deposit must be positive.")
        self._balance += a

    def withdraw(self, amount: float) -> None:
        a = float(amount)
        if a <= 0.0:
            raise ValueError("Withdraw must be positive.")
        # Validation rule: must have sufficient funds
        if a > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= a


acc = BankAccount(1000)
print("Start:", acc.get_balance())
acc.deposit(250)
print("After deposit:", acc.get_balance())
try:
    acc.withdraw(2000) # Test insufficient funds
except ValueError as e:
    print("Invalid withdraw blocked:", e)
acc.withdraw(500)
print("After withdraw:", acc.get_balance())


# ==============================================================================
# 5) CAFETERIA ACCOUNT — REFACTOR to encapsulation (Bad vs Good)
# ==============================================================================

print(SECTION + "5) CAFETERIA ACCOUNT (bad vs good)")

class BadCafeteriaAccount:
    # Anti-example: balance is public; anyone can write junk into it.
    def __init__(self, balance: int = 0):
        self.balance = balance  # BAD: direct public field

class GoodCafeteriaAccount:
    # Fix with encapsulation: use methods to control internal _balance.
    def __init__(self, balance: int = 1000):
        self._balance = int(balance)

    def get_balance(self) -> int:
        return self._balance

    def top_up(self, amount: int) -> None:
        a = int(amount)
        if a <= 0:
            raise ValueError("Top-up amount must be positive.")
        self._balance += a

    def pay(self, amount: int) -> None:
        a = int(amount)
        if a <= 0:
            raise ValueError("Payment must be positive.")
        if a > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= a


bad = BadCafeteriaAccount(1000)
bad.balance = -999  # Demonstration of bad practice: bypassing rules
print("BAD design allows this:", bad.balance)

good = GoodCafeteriaAccount()
good.pay(200)
print("After lunch:", good.get_balance())
good.top_up(500)
print("After top-up:", good.get_balance())

# WARNING demo: Direct internal poke is still possible but discouraged:
good._balance = -999
print("Direct poke (discouraged):", good._balance)


# ==============================================================================
# 6) LIBRARY BOOK — stock control
# ==============================================================================

print(SECTION + "6) LIBRARY BOOK (no negative copies)")

class LibraryBook:
    def __init__(self, title: str, copies: int = 1):
        self.title = title
        self._copies = int(copies)

    def get_copies(self) -> int:
        return self._copies

    def available(self) -> bool:
        return self._copies > 0

    def borrow_one(self) -> bool:
        # Rule: only decrease if copies > 0
        if self._copies > 0:
            self._copies -= 1
            return True
        return False

    def return_one(self) -> None:
        self._copies += 1


b = LibraryBook("Clean Code", copies=1)
print("Available?", b.available(), "| copies:", b.get_copies())
print("Borrow success:", b.borrow_one(), "| copies:", b.get_copies())
print("Borrow again:", b.borrow_one(), "| copies:", b.get_copies())
b.return_one()
print("After return:", b.get_copies())


# ==============================================================================
# 7) HOSTEL VISITOR LOG — Encapsulation for Complex Logic
# ==============================================================================

print(SECTION + "7) HOSTEL LOG (dict & set only)")

class Visitor:
    def __init__(self, name: str, visitor_id: str):
        self.name = name
        self.visitor_id = visitor_id

class Resident:

# encapsulation_examples.py
# Demonstrates visibility, classic getters/setters, validation, and read-only attributes.

from datetime import datetime

SECTION = "\n" + "=" * 72 + "\n"

# ==============================================================================
# 0) VISIBILITY: public / _protected / __private
# ==============================================================================

class VisibilityDemo:
    def __init__(self):
        # Public: everyone can read/write directly.
        self.public_attr = "PUBLIC"
        
        # Protected (by convention): convention suggests 'internal use only'.
        self._protected_attr = "PROTECTED (convention)"
        
        # Pseudo-Private: name-mangled by Python (harder to access accidentally).
        self.__private_attr = "PRIVATE (name-mangled)"

    def reveal_private(self):
        # The proper way: access private attributes INSIDE the class method.
        return self.__private_attr


# DEMO: what you can access from outside
print(SECTION + "0) VISIBILITY: public / _protected / __private")
v = VisibilityDemo()

# Public access:
print("Public:", v.public_attr)

# Protected access (allowed, but discouraged by convention):
print("Protected (by convention):", v._protected_attr)

# Private access via method (proper way):
print("Private via method:", v.reveal_private())

# Private access via name-mangling (discouraged, but possible):
print("Private via name-mangling:", v._VisibilityDemo__private_attr)


# ==============================================================================
# 1) CLASSIC GETTERS/SETTERS (no @property)
# ==============================================================================

print(SECTION + "1) GETTERS/SETTERS (no @property)")

class CourseClassic:
    def __init__(self, name: str):
        # Use _ convention for internal storage.
        self._name = name

    def get_name(self) -> str:
        # Getter: Safe read.
        return self._name

    def set_name(self, new_name: str) -> None:
        # Setter: Safe write with validation.
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = new_name.strip()


c = CourseClassic("OOP")
print("get_name:", c.get_name())
c.set_name("Encapsulation")
print("after set_name:", c.get_name())


# ==============================================================================
# 2) STUDENT — GPA WITH VALIDATION
# ==============================================================================

print(SECTION + "2) STUDENT GPA (classic getters/setters)")

class Student:
    def __init__(self, name: str, gpa: float = 0.0):
        self.name = name
        self._gpa = 0.0          # internal storage
        self.set_gpa(gpa)        # Use the setter even in __init__ for validation

    def get_gpa(self) -> float:
        return self._gpa

    def set_gpa(self, value: float) -> None:
        v = float(value)
        # Validation rule: GPA must be between 0.0 and 5.0
        if not (0.0 <= v <= 5.0):
            raise ValueError("GPA must be between 0.0 and 5.0")
        self._gpa = v

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, GPA: {self.get_gpa():.2f}"


s = Student("Aisha", 4.4)
print(s.introduce())
try:
    s.set_gpa(6.7)    # Test the validation
except ValueError as e:
    print("Invalid GPA blocked:", e)


# ==============================================================================
# 3) TEMPERATURE — read-only computed values
# ==============================================================================

print(SECTION + "3) TEMPERATURE (computed read-only)")

class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._celsius = 0.0
        self.set_celsius(celsius)

    def set_celsius(self, value: float) -> None:
        v = float(value)
        # Validation rule: cannot go below absolute zero
        if v < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = v

    def get_celsius(self) -> float:
        return self._celsius

    def get_fahrenheit(self) -> float:
        # Computed attribute (read-only)
        return (self._celsius * 9.0 / 5.0) + 32.0

    def get_kelvin(self) -> float:
        # Computed attribute (read-only)
        return self._celsius + 273.15


t = Temperature(25)
print("C:", t.get_celsius(), "F:", round(t.get_fahrenheit(), 2), "K:", round(t.get_kelvin(), 2))
try:
    t.set_celsius(-500)  # Test the validation
except ValueError as e:
    print("Invalid celsius blocked:", e)


# ==============================================================================
# 4) BANK ACCOUNT — encapsulated balance
# ==============================================================================

print(SECTION + "4) BANK ACCOUNT (safe updates only)")

class BankAccount:
    def __init__(self, balance: float = 0.0):
        self._balance = float(balance)

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        a = float(amount)
        if a <= 0.0:
            raise ValueError("Deposit must be positive.")
        self._balance += a

    def withdraw(self, amount: float) -> None:
        a = float(amount)
        if a <= 0.0:
            raise ValueError("Withdraw must be positive.")
        # Validation rule: must have sufficient funds
        if a > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= a


acc = BankAccount(1000)
print("Start:", acc.get_balance())
acc.deposit(250)
print("After deposit:", acc.get_balance())
try:
    acc.withdraw(2000) # Test insufficient funds
except ValueError as e:
    print("Invalid withdraw blocked:", e)
acc.withdraw(500)
print("After withdraw:", acc.get_balance())


# ==============================================================================
# 5) CAFETERIA ACCOUNT — REFACTOR to encapsulation (Bad vs Good)
# ==============================================================================

print(SECTION + "5) CAFETERIA ACCOUNT (bad vs good)")

class BadCafeteriaAccount:
    # Anti-example: balance is public; anyone can write junk into it.
    def __init__(self, balance: int = 0):
        self.balance = balance  # BAD: direct public field

class GoodCafeteriaAccount:
    # Fix with encapsulation: use methods to control internal _balance.
    def __init__(self, balance: int = 1000):
        self._balance = int(balance)

    def get_balance(self) -> int:
        return self._balance

    def top_up(self, amount: int) -> None:
        a = int(amount)
        if a <= 0:
            raise ValueError("Top-up amount must be positive.")
        self._balance += a

    def pay(self, amount: int) -> None:
        a = int(amount)
        if a <= 0:
            raise ValueError("Payment must be positive.")
        if a > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= a


bad = BadCafeteriaAccount(1000)
bad.balance = -999  # Demonstration of bad practice: bypassing rules
print("BAD design allows this:", bad.balance)

good = GoodCafeteriaAccount()
good.pay(200)
print("After lunch:", good.get_balance())
good.top_up(500)
print("After top-up:", good.get_balance())

# WARNING demo: Direct internal poke is still possible but discouraged:
good._balance = -999
print("Direct poke (discouraged):", good._balance)


# ==============================================================================
# 6) LIBRARY BOOK — stock control
# ==============================================================================

print(SECTION + "6) LIBRARY BOOK (no negative copies)")

class LibraryBook:
    def __init__(self, title: str, copies: int = 1):
        self.title = title
        self._copies = int(copies)

    def get_copies(self) -> int:
        return self._copies

    def available(self) -> bool:
        return self._copies > 0

    def borrow_one(self) -> bool:
        # Rule: only decrease if copies > 0
        if self._copies > 0:
            self._copies -= 1
            return True
        return False

    def return_one(self) -> None:
        self._copies += 1


b = LibraryBook("Clean Code", copies=1)
print("Available?", b.available(), "| copies:", b.get_copies())
print("Borrow success:", b.borrow_one(), "| copies:", b.get_copies())
print("Borrow again:", b.borrow_one(), "| copies:", b.get_copies())
b.return_one()
print("After return:", b.get_copies())


# ==============================================================================
# 7) HOSTEL VISITOR LOG — Encapsulation for Complex Logic
# ==============================================================================

print(SECTION + "7) HOSTEL LOG (dict & set only)")

class Visitor:
    def __init__(self, name: str, visitor_id: str):
        self.name = name
        self.visitor_id = visitor_id

class Resident:
    def __init__(self, name: str, room_no: str):
        self.name = name
        self.room_no = room_no

class Hostel:
    def __init__(self, name: str, max_visits_per_day: int = 100):
        self.name = name
        self._log = {}                 # Internal storage: timestamp -> string line
        self._visit_count_today = 0
        self._max_visits_per_day = int(max_visits_per_day)
        self._blacklist_ids = set()    # Internal storage: for set operations

    def blacklist_add(self, visitor_id: str) -> None:
        self._blacklist_ids.add(visitor_id)

    def reset_daily_count(self) -> None:
        self._visit_count_today = 0

    def record_visit(self, visitor: Visitor, resident: Resident) -> None:
        # Logic/Validation rules encapsulated here:
        if not visitor.name.strip() or not resident.name.strip():
            raise ValueError("Names must not be empty.")
        if visitor.visitor_id in self._blacklist_ids:
            raise PermissionError("This visitor is blacklisted.")
        if self._visit_count_today >= self._max_visits_per_day:
            raise RuntimeError("Daily visit limit reached.")

        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry_str = f"{visitor.name} -> {resident.name} (Room {resident.room_no})"
        self._log[ts] = entry_str
        self._visit_count_today += 1

    def show_visits(self) -> None:
        print(f"Visit log for {self.name} Hostel:")
        if not self._log:
            print("  (No visits yet)")
            return
        # Displaying data from internal storage (_log)
        for ts in sorted(self._log.keys()):
            print(" - " + ts + ": " + self._log[ts])

    def search_by_visitor(self, name_substr: str) -> dict:
        # Provides safe, controlled access to log data
        result = {}
        target = name_substr.lower()
        for ts in sorted(self._log.keys()):
            val = self._log[ts]
            if target in val.lower():
                result[ts] = val
        return result


h = Hostel("UCU", max_visits_per_day=3)
h.blacklist_add("BANNED1")
h.record_visit(Visitor("Alice", "V123"), Resident("Bob", "12B"))
h.record_visit(Visitor("Allan", "V129"), Resident("Brian", "2C"))
h.record_visit(Visitor("Charles", "V777"), Resident("Diana", "2A"))
h.show_visits()
print("Search 'Ali':", h.search_by_visitor("Ali"))

# simple_greeting.py
# Prints "Good Morning", "Good Afternoon", or "Good Evening" based on the system time.

from datetime import datetime

# Get the current hour (24-hour clock)
hour = datetime.now().hour

# Check the time range to determine the appropriate greeting
if hour < 12:
    print("Good Morning")
elif hour < 18:
    print("Good Afternoon")
else:
    print("Good Evening")
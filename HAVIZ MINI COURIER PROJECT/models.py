from typing import Tuple  # This helps Python know what types of things we're using, like lists or numbers.

# This is a "mixin" – think of it as a superpower that classes can borrow.
class Identifiable:
    """Mixin for objects with an ID. Like giving everything a name tag."""
    def get_id(self) -> str:
        raise NotImplementedError  # Means "you must fill this in when you use it!"

class Printable:
    """Mixin for objects that can be printed as a row. Like turning info into a table row."""
    def to_row(self) -> Tuple:
        raise NotImplementedError

# A Hub is like a store or library where deliveries start.
class Hub(Identifiable, Printable):
    """Represents a hub on campus. Like Haviz Cafe or a hostel."""
    def __init__(self, hub_id: str, hub_name: str, campus: str):
        self.hub_id = hub_id  # Unique name, like "H1"
        self.hub_name = hub_name  # Friendly name, like "Haviz Cafe"
        self.campus = campus  # Where it's located, like "Bugujju"

    def get_id(self) -> str:
        return self.hub_id

    def to_row(self) -> Tuple[str, str, str]:
        return (self.hub_id, self.hub_name, self.campus)  # For printing in a table

    def __repr__(self) -> str:
        return f"Hub(hub_id={self.hub_id}, hub_name={self.hub_name}, campus={self.campus})"  # How it looks when printed

# A Parcel is like a package: coffee, jeans, or a book.
class Parcel(Identifiable, Printable):
    """Represents a parcel to be delivered. Like a box of pastries."""
    def __init__(self, parcel_id: str, recipient: str, priority: str, hub_id: str, destination: str, weight_kg: float):
        self.parcel_id = parcel_id  # Unique ID, like "P1"
        self.recipient = recipient  # Who gets it, like "Student A"
        self.priority = priority.upper()  # "EXPRESS" (fast) or "NORMAL" (chill), always uppercase
        self.hub_id = hub_id  # Where it starts, like from Haviz Cafe
        self.destination = destination  # Where it goes, like "Sabiiti" hostel
        self.weight_kg = weight_kg  # How heavy, in kg

    def get_id(self) -> str:
        return self.parcel_id

    def to_row(self) -> Tuple[str, str, str, str, str, float]:
        return (self.parcel_id, self.recipient, self.priority, self.hub_id, self.destination, self.weight_kg)

    def __repr__(self) -> str:
        return f"Parcel(parcel_id={self.parcel_id}, recipient={self.recipient}, priority={self.priority}, hub_id={self.hub_id}, destination={self.destination}, weight_kg={self.weight_kg})"

# A Rider is like a delivery guy: Sunday from JLuxe or Cole from the library.
class Rider(Identifiable, Printable):
    """Represents a delivery rider. Like the guy on a boda or walking."""
    def __init__(self, rider_id: str, name: str, max_load_kg: float, home_hub_id: str):
        self.rider_id = rider_id  # Unique ID, like "R1"
        self.name = name  # Name, like "Sunday"
        self.max_load_kg = max_load_kg  # Max weight they can carry, like 15kg for bodas, 5kg for walking
        self.home_hub_id = home_hub_id  # Their starting hub, like JLuxe

    def get_id(self) -> str:
        return self.rider_id

    def to_row(self) -> Tuple[str, str, float, str]:
        return (self.rider_id, self.name, self.max_load_kg, self.home_hub_id)

    def __repr__(self) -> str:
        return f"Rider(rider_id={self.rider_id}, name={self.name}, max_load_kg={self.max_load_kg}, home_hub_id={self.home_hub_id})"

# Personalization: Special pickup spots, like kiosks or lockers at hostels.
class PickupPoint(Identifiable, Printable):
    """Base class for pickup points. Like a locker where you grab stuff."""
    def __init__(self, pickup_id: str, hub_id: str, label: str, base_priority_bias: int = 0):
        self.pickup_id = pickup_id  # Unique ID
        self.hub_id = hub_id  # Linked to a hub
        self.label = label  # Name, like "Kiosk at Sabiiti"
        self.base_priority_bias = base_priority_bias  # Bonus points for priority (higher = faster delivery)

    def get_id(self) -> str:
        return self.pickup_id

    def to_row(self) -> Tuple[str, str, str, int]:
        return (self.pickup_id, self.label, self.hub_id, self.base_priority_bias)

    def __repr__(self) -> str:
        return f"PickupPoint(pickup_id={self.pickup_id}, hub_id={self.hub_id}, label={self.label}, base_priority_bias={self.base_priority_bias})"

# Subclasses: Different types of pickups with their own biases.
class CampusKiosk(PickupPoint):
    """Pickup at campus kiosks, slight priority boost. Like a quick-stop spot."""
    def __init__(self, pickup_id: str, hub_id: str, label: str):
        super().__init__(pickup_id, hub_id, label, base_priority_bias=1)  # +1 means a bit faster

class DormLocker(PickupPoint):
    """Pickup at dorm lockers, neutral bias. Normal speed."""
    def __init__(self, pickup_id: str, hub_id: str, label: str):
        super().__init__(pickup_id, hub_id, label, base_priority_bias=0)  # No bonus

class OfficeDesk(PickupPoint):
    """Pickup at office desks, slight priority reduction. A bit slower."""
    def __init__(self, pickup_id: str, hub_id: str, label: str):
        super().__init__(pickup_id, hub_id, label, base_priority_bias=-1)  # -1 means slower
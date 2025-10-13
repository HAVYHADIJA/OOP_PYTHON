import math

# Define a Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Calculate the distance between two points
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    # Find the midpoint between two points
    def midpoint(self, other):
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Point(mid_x, mid_y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Define a Circle class
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    # Calculate area of the circle
    def area(self):
        return math.pi * (self.radius ** 2)

    # Check if a point lies inside or on the circle
    def contains(self, point):
        return self.center.distance_to(point) <= self.radius

    # Stretch goal: check if circles intersect
    def intersects(self, other_circle):
        distance_between_centers = self.center.distance_to(other_circle.center)
        return distance_between_centers <= (self.radius + other_circle.radius)

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"


# -------- TESTING --------
# Create a circle
circle1 = Circle(Point(0, 0), 5)

# Create some points
points = [Point(1, 1), Point(4, 4), Point(6, 0), Point(0, 5)]

# Check which points are inside the circle
for p in points:
    print(f"{p} inside circle? {circle1.contains(p)}")

# Midpoint and distance example
p1 = Point(2, 3)
p2 = Point(4, 7)
print(f"Distance between {p1} and {p2} = {p1.distance_to(p2):.2f}")
print(f"Midpoint = {p1.midpoint(p2)}")

# Stretch: check circle intersection
circle2 = Circle(Point(8, 0), 4)
print(f"{circle1} intersects {circle2}? {circle1.intersects(circle2)}")

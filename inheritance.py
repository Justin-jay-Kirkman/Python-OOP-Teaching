"""
    Inheritance is the sharing of information from a parent to a child; It Inherits all the methods and properties.
    EXAMPLES
        1. Single level inheritance
        2. Multilevel inheritance
        3. Multiple inheritance
"""


# single level
class Attraction:  # Base class (Parent)
    def __init__(self, name):
        self.name = name


class Ride(Attraction):  # Derived class (child)
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Ride'

    def describe(self):
        print(f"{self.name} | {self.type}")


class ShowAndFireworks(Attraction):  # Derived class (child)
    def __init__(self, name, times):
        super().__init__(name)
        self.name = name
        self.type = 'Show'
        self.times = times

    def describe(self):
        print(f"{self.name} | {self.type} | {self.times}")


# multi level inheritance
class Rollercoaster(Ride):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Rollercoaster'


# Multiple inheritance -
# Use this sparingly as can lead to a class that inherits from two classes that share an ancestor - Diamond issue
class HeightRequirement:
    def __init__(self, height=0):
        self.height = height

    def display_height_requirement(self):
        if self.height > 0:
            print(f"Height requirement is {self.height}")
        else:
            print(f"There is no height requirement")


class RideWithHeightRequirement(Ride, HeightRequirement):
    def __init__(self, name, height=0):
        Ride.__init__(self, name)
        HeightRequirement.__init__(self, height)
        self.type = 'RideWithHeightRequirement'

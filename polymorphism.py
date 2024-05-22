"""
polymorphism is the redefining of information - AKA Many - changes in form
    EXAMPLES:
    1. Duck Typing
    2. Method Overwriting
    3. Method Overloading
    4. Operator Overloading
"""
import copy


# Duck Typing
class Attraction:  # Base class (Parent)
    def __init__(self, name):
        self.name = name

    #2. This method is overwritten by children
    def describe(self):
        NotImplemented


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

    #3. Method overloading doesn't exsist in python, but you can add multiple arguments and just ignore ones you don't use
    def add_times(self, *args):
        for times in args:
            self.times.append(times)

    #4. operator overloading, this will allow you to + two objects together
    def __add__(self, other):
        both_times = copy.copy(self.times)
        both_times.extend(other.times)
        return ShowAndFireworks(f"{self.name} and {other.name}", both_times)


#1. Duck typing, because both objects have describe, this works
def describeObj(obj):
    obj.describe()




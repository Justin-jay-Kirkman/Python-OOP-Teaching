# Hiding of information within a class; Blueprint of a class for others to inherit

from abc import abstractmethod, ABCMeta


class Location(metaclass=ABCMeta):
    @abstractmethod
    def get_address(self):
        return "This cannot be reached as it is an abstract method"


class ThemePark(Location):
    def __init__(self, address):
        self.address = address

    def get_address(self):
        return self.address


class Office(Location):
    def __init__(self, address):
        self.address = address

    def get_address(self):
        return self.address

    #overide the '+' for Office
    def __add__(self, other):
        return Office(f"{self.address} and {other.address}")

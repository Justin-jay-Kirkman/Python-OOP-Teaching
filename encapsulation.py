# 2: encapsulation -  Grouping of information within a class to hide the details from the user
from inheritance import Ride, ShowAndFireworks

# The layers of attractions
class ThemePark:
    def __init__(self, name):
        self.name = name
        self.attraction = []

    def add_attraction(self, attraction):
        self.attraction.append(attraction)

    def add_attractions(self, *args):
        for attraction in args:
            self.add_attraction(attraction)

    def display_attractions(self):
        for attraction in self.attraction:
            attraction.describe()

    def display_rides(self):
        for ride in self.attraction:
            if isinstance(ride, Ride):
                ride.describe()

    def display_showand_fireworks(self):
        for firework in self.attraction:
            if isinstance(firework, ShowAndFireworks):
                firework.describe()


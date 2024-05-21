from inheritance import RideWithHeightRequirement, Rollercoaster, Ride, ShowAndFireworks
from encapsulation import ThemePark

avatarFlight = Ride("Avatar Flight of Passage")
beautyAndBeast = ShowAndFireworks("Beauty and the Beast – Live on Stage", ["11:00AM", "1:00PM", "2:00PM"])
bigThunder = Rollercoaster("Big Thunder Mountain Railroad")

gangplank_falls = RideWithHeightRequirement("Gangplank Falls")

disneyWorld = ThemePark("Disney")
disneyWorld.add_attraction(beautyAndBeast)
disneyWorld.add_attractions(avatarFlight, bigThunder, gangplank_falls)

print("\nDisplay attractions")
disneyWorld.display_attractions()

print("\nDisplay rides")
disneyWorld.display_rides()

print("\nDisplay show and fireworks")
disneyWorld.display_showand_fireworks()
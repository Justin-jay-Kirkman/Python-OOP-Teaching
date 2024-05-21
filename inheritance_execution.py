from inheritance import RideWithHeightRequirement, Rollercoaster, Ride, ShowAndFireworks

print("\nSingle Layer Inheritance")
ride = Ride("Avatar Flight of Passage")
ride.describe()

show = ShowAndFireworks("Beauty and the Beast – Live on Stage", ["11:00AM", "1:00PM", "2:00PM"])
show.describe()

print("\nMulti-layer inheritance")
rollercoaster = Rollercoaster("Big Thunder Mountain Railroad")
rollercoaster.describe()


print("\nMultiple inheritance")
ride_w_requirements = RideWithHeightRequirement("Avatar Flight of Passage", 44)
ride_w_requirements.describe()
ride_w_requirements.display_height_requirement()

gangplank_falls = RideWithHeightRequirement("Gangplank Falls")
gangplank_falls.describe()
gangplank_falls.display_height_requirement()

# Extra fun
print("\nFind rides with no height requirement")
list_of_rides = []
list_of_rides.append(ride_w_requirements)
list_of_rides.append(gangplank_falls)

for ride in list_of_rides:
    if ride.height == 0:
        print(ride.name)
from polymorphism import Ride, ShowAndFireworks, describeObj

ride = Ride("Avatar Flight of Passage")
beauty_and_beast = ShowAndFireworks("Beauty and the Beast – Live on Stage", ["11:00AM", "1:00PM", "2:00PM"])
fantasmic = ShowAndFireworks("fantasmic", [])

print("\n1. Duck Typing")
describeObj(ride)
describeObj(fantasmic)
describeObj(beauty_and_beast)
print("\n2. Method Overwriting")
ride.describe()
print("\n3. Method Overloading")
fantasmic.describe()
fantasmic.add_times("9:00PM")
fantasmic.describe()

print("\n4. Operator Overloading")
both_shows = beauty_and_beast + fantasmic

both_shows.describe()
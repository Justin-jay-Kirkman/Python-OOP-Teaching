from abstraction import ThemePark, Office, Location

theme_park = ThemePark('111 test address')
print(theme_park.get_address())
office = Office('555 test address')
print(office.get_address())

both_locations = office + theme_park
print(both_locations.get_address())

# You cannot use the addition as theme_park doesn't have an __add__ override
# both_locations = theme_park + office
# print(both_locations.get_address())

# This would error as abstract classes can't be instantiated
# location = Location()
# location.get_address()

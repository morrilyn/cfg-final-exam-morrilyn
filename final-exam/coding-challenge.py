class Planet:
    
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        distance_from_earth = self.distance_from_sun - 147000000
        return distance_from_earth

#question 2 
    
class Mercury(Planet):
    @staticmethod
    def happy_new_year():
        return "A year on Mercury lasts 88 Earth days."

mercury = Mercury('Mercury', 58000000, 'Terrestrial')


#question 3
class Jupiter(Planet):
    def __init__(self, name, distance_from_sun, planet_type, number_of_moons):
       
        super().__init__(name, distance_from_sun, planet_type)
      
        self.number_of_moons = number_of_moons
    @staticmethod
    def happy_new_year():
        return "A year on Jupiter lasts 4383 Earth days."

mercury = Mercury('Mercury', 58000000, 'Terrestrial')
jupiter = Jupiter('Jupiter', 779000000, 'Gas Giant', 80)


# Print info for Mercury

print(f'Name: {mercury.name}')
print(f'Planet Distance: {mercury.distance_from_sun}')
print(f'Planet Type: {mercury.planet_type}')
print(f'Distance to earth (km): {mercury.get_distance_to_earth()}')
print(Mercury.happy_new_year())

# Print info for Jupiter

print(f'Name: {jupiter.name}')
print(f'Planet Distance: {jupiter.distance_from_sun}')
print(f'Planet Type: {jupiter.planet_type}')
print(f'Number of Moons: {jupiter.number_of_moons}')
print(f'Distance to earth (km): {jupiter.get_distance_to_earth()}')
print(Jupiter.happy_new_year())


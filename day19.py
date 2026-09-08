# freeCodeCamp
class Planet:
    def __init__(self, name, planet_type, star):
        
        

        if type(name) is not str or type(planet_type) is not str or type(star) is not str:
            raise TypeError('name, planet type, and star must be strings')

        if not name or not planet_type or not star:
            raise ValueError('name, planet_type, and star must be non-empty strings')

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet('earth', 'solid', 'sun')
planet_2 = Planet('proxima b', 'solid', 'proxima')
planet_3 = Planet('jupiter', 'gas giant', 'sun')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())


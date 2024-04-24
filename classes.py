from space.planet import Planet
from space.calc import planet_mass, planet_wall

hoth = Planet('Hoth', 20000, 5.4, 'Hoth System')
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The Gravity is: {hoth.gravity }')
print(hoth.orbit())

planetX = Planet('Naboo', 2300, 5.2, 'Nabooo system')
print(planetX.orbit()) 
print(hoth.spin('a very high speed'))

planetX_mass = planet_mass(planetX.gravity, planetX.radius)
print(planetX_mass)
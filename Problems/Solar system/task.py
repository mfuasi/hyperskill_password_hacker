# create the planets.txt
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file = open('planets.txt', 'w', encoding='utf-8')

for planet in planets:
    file.write('{}\n'.format(planet))

file.close()

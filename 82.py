# Question: Use Python to calculate the distance in kilometers between Jupiter and Sun on January 1, 1230.

import ephem
jupyter = ephem.Jupiter()
jupyter.compute('1230/1/1')
distance_au_units = jupyter.sun_distance
distance_km = distance_au_units * 149597870.691
print(distance_km)

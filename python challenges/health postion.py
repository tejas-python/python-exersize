import random
health = 50
difficulty = 2
portion_health = int(random.randint(25, 50)/difficulty)
health = health+portion_health
print(health)

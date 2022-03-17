# generate a 6 digit pasword

import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

choose = random.sample(characters,6)
print("".join(choose))

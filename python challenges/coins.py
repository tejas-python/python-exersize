
import random

from click import option 

class Pound:
    '''create coin class'''
    def __init__(self,rare=False): # constructutor

        self.rare = rare 
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.value = 1.0
        self.color = 'gold'
        self.num_edges = 1
        self.diamter = 22.5#mm
        self.thickness = 3.15 #mm
        self.heads = True
    def rust(self):
        self.color ='greenish'
    def clean(self):
        self.colour = "gold"
    def flip(self):
        options = [True,False]
        choice  = random.choice(options)
        self.head = choice
    def __del__(self): # destructuor to deete the object 
        print("coin spent")

coin1 = Pound()


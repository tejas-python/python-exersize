
import random

class Coin:
    def __init__(self,rare = True,clean=True,heads= True,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        self.is_rare = rare
        self.is_clean= clean
        self.head = heads
        if self.is_rare:
            self.value = self.original_value *1.25
        else:
            self.value = self.original_value 
        if self.is_clean:
            self.color   = self.clean_colour
        else:
            self.color = self.rusty_colour
        def rust(self):
            self.color =self.rusty_colour
        def clean(self):
            self.colour = self.clean_colour

        def __del__(self): # destructuor to deete the object 
            print("coin spent")  
        def flip(self):
            options = [True,False]
            choice  = random.choice(options)
            self.head = choice

# class Pound(Coin): #inhertitence 
#     def __init__(self):
#         data = {'original_value': 1.00,"clean_colour":"gold","rusty_colour":"greenish",
#         "num_edges":1,
#         "diameter":22.5,
#         "thickness":3.15,
#         "mass":9.5}
#         super.__init__(**data)

class one_pence(Coin): #inhertitence 
    def __init__(self):
        data = {'original_value': 0.01,"clean_colour":"bronze","rusty_colour":"brownish",
        "num_edges":1,
        "diameter":20.5,
        "thickness":1.15,
        "mass":3.56}
        super.__init__(**data)



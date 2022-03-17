# Question: Please download the file in the attachment and use Python to print out its content. company1.json

import json
from pprint import pprint
file = open('company1.json','r')
d = json.load(file)
pprint(d)

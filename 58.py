import json
from pprint import pprint
file = open('company1.json','r+')
d = json.loads(file.read())
d['employees'].append({"firstName": "irom ", "lastName": "man"})
file.seek(0)
json.dump(d,file,indent=4,sort_keys=True)
pprint(d)
file.close()

# Question: Store the dictionary in a json file.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
import json
# json_dict =
with open("company1.json",'w') as file:
    json.dump(d,file,indent=4)
print("done")

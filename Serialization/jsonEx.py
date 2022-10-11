from cgi import test
from io import StringIO
import json
import requests

# Encoding JSON (Serialization)

# data = {
#     "user": {
#         "name": "William Williams",
#         "age": 93
#     }
# }

# with open("Serialization/data_file.json", "w") as write_file:
#     json.dump(data, write_file, indent=4) # Add argument to add indent
    
# json_str = json.dumps(data, indent=4) # To used the json data
# print(json_str)

# Decoding JSON

# Why is json.load(read_json) does not work?
# Because we only read once...

# load (to get from a text file)
# loads (to get from json document)
# with open("Serialization/data_file.json") as read_json:
#     data = json.load(read_json)
#     print(data)

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
test = json.loads(json_string)
print(json.dumps(test, indent = 4, sort_keys=True))

### EXAMPLE 1 ###
# result in python dictionary
with open("Serialization/stats.json", "r") as read_file:
    data = json.load(read_file)
    # loads commonly used for JSON obtain from web document

decoded_children = data["children"]
print("What the person first Name?: " + data["firstName"])
print("What the person last name?: " + data["lastName"])
print(" What is the person age? " + str(data["age"]))
# Printing List from JSON

for hobbies in data["hobbies"]:
    print("What is the person hobby?: " + hobbies)

print("Type: ", type(data["children"]))
if (data["children"]):
    print ("This person has children")
    for children in data['children']:
        print("The children first name: " + children["firstName"])
else:
    print("This person does not have children")
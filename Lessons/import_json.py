import json

dictionary = {
    "user_name": "Albert",
    "password": "123",
    "host": "127.0.0.1"
}

json_object = json.dumps(dictionary, indent=4)

print(type(json_object))       # <class 'str'>
print(json_object)

with open('sample.json', 'w') as outfile:
    outfile.write(json_object)

import yaml

list1 = [
    {
        "user_name": "Albert",
        "password": "123",
        "host": "127.0.0.1"
    },
    {
        "user_name": "test",
        "password": "321",
        "host": "127.0.0.1"
    }
]

with open('list1.yaml', 'w') as file:
    yaml.dump(list1, file)

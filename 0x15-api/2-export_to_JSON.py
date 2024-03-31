#!/usr/bin/python3
"""
export in Json
"""


if __name__ == "__main__":
    import requests
    import json
    from sys import argv


    id = int(argv[1])
    values = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    task = 0
    total = 0
    dump_dict = {}


    for value in values:
        if value["userId"] == id:
            total += 1
            if value["completed"]:
                task += 1

    for user in users:
        if user['id'] == id:
            dump_dict[id] = []
            for value in values:
                if value['userId'] == id:
                    dump_dict[id].append({"task": value['title'],
                                          "completed": value['completed'],
                                          "username": user['username']})

    with open("{}.json".format(id), "a+") as csvfile:
        json.dump(dump_dict, fp=csvfile)

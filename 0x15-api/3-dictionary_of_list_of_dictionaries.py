#!/usr/bin/python3
"""_summary_"""


if __name__ == "__main__":
    import requests
    import json
    values = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    done = 0
    total = 0
    dump_dict = {}

    for value in values:
        if value['userId'] == id:
            total += 1
            if value['completed']:
                done += 1

    for user in users:
        dump_list = []
        for value in values:
            if value['userId'] == user['id']:
                dump_list.append({"username": user['username'],
                                  "task": value['title'],
                                  "completed": value['completed']})
        dump_dict[user['id']] = dump_list
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(dump_dict, fp=jsonfile)

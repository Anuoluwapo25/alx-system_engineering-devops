#!/usr/bin/python3
"""_summary_"""


if __name__ == "__main__":
    import requests
    from sys import argv

    id = int(argv[1])
    users = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/users").json()
    task  = 0
    total = 0

    for value in users:
        if value['userId'] == id:
            total += 1
            if value['completed']:
                task += 1

    for user in tasks:
        if user['id'] == id:
            print("Employee {} is done with tasks({}/{}):"
                  .format(user['name'], task, total))
            for value in users:
                if value['userId'] == id and value['completed']:
                    print("\t {}".format(value['title']))

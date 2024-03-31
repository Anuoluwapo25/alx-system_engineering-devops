#!/usr/bin/python3
"""_summary_"""


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    id = int(argv[1])
    values = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    done = 0
    total = 0

    for value in values:
        if value['userId'] == id:
            total += 1
            if value['completed']:
                done += 1

    for user in users:
        if user['id'] == id:
            with open("{}.csv".format(id), "a+") as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for value in values:
                    if value['userId'] == id:
                        itr = [user['id'],
                               user['username'],
                               value['completed'],
                               value['title']]
                        writer.writerow(itr)

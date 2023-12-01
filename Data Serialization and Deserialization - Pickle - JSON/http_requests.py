import requests
import csv

respond = requests.get('https://jsonplaceholder.typicode.com/users')

persons_list = respond.json()  # json.loads(respond.text) the same list object, needs to import json

with open('persons.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # write a header to file
    writer.writerow(['Name', "GPS of(LAT, LNG)", 'Company'])

    for person in persons_list:
        data = [
            f"{person['name']},"
            f"{person['address']['city']},"
            f"({person['address']['geo']['lat']},{person['address']['geo']['lng']}),"
            f"{person['company']['name']}"
        ]
        writer.writerow(data)


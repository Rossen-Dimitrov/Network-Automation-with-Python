import csv

people = [
    ['Dan', 34, 'Bucharest'],
    ['Andrei', 21, 'London'],
    ['Maria', 45, 'Paris']
]

with open('people1.csv', 'w') as f:
    writer = csv.writer(f, delimiter=":")
    for line in people:
        writer.writerow(line)

with open('people1.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        print(r)

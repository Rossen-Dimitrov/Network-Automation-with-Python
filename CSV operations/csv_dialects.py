import csv

csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

with open('items.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, dialect='hashes')
    for row in reader:
        print(row)

with open('items.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))


# print(csv.list_dialects()) #['excel', 'excel-tab', 'unix']
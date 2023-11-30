import csv

with open('airtravel.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    csv_data = ("NEW_DATA", 111, 222, 333)
    writer.writerow(csv_data)

with open('number.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x ** 2, x ** 3, x ** 4])

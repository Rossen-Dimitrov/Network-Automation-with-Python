import csv
import pandas as pd

with open('airtravel.csv') as f:
    reader = csv.reader(f)
    next(reader)  # skips the header row
    year_1958 = {}

    for row in reader:
        year_1958[row[0]] = int(row[1])  # Convert the value to an integer

    df = pd.DataFrame(year_1958.items(), columns=['Month', 'Passengers'])
    print(df)

    max_value = max(year_1958, key=year_1958.get)
    print(f"Month with the maximum passengers in 1958: {max_value}, Passengers: {year_1958[max_value]}")


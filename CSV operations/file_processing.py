import csv

result = []
with open('devices.txt', 'r') as f:
    reader = csv.reader(f, delimiter=':')
    [result.append(row) for row in reader]
    print(result)


# with open('devices.txt', 'r') as f:
#     devices = f.read().splitlines()
#
# result = []
# for item in devices:
#     tmp = item.split(';')
#     result.append(tmp)
#
# print(result)

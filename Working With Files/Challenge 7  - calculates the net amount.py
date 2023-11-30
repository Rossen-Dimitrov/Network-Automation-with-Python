def calculate(file):
    transactions = {
        'D': 0,
        'W': 0,
    }
    with open(file, 'r') as f:
        content = f.read().splitlines()
        for row in content:
            split = row.split(':')
            tr_type, amount = split[0], int(split[1])
            transactions[tr_type] += amount
        print(transactions['D'] - transactions['W'])


calculate('banking.txt')

with open('macs.txt') as f:
    all_macs = f.read().split()
    unique_macs = list(set(all_macs))


with open('unique_macs.txt', 'w', newline='') as f:
    f.write('\n'.join(unique_macs))

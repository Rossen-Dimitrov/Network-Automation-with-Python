from netmiko import ConnectHandler
import getpass

password = getpass.getpass('Enter password:')

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.88.10',
    'username': 'ross',
    'password': password,
    'port': 22,
    'secret': '1212',
    'verbose': True
}
connection = ConnectHandler(**cisco_device)
prompter = connection.find_prompt()
print(prompter[:-1])
if '>' in prompter:
    connection.enable()
print(f"{cisco_device['host']}:{cisco_device['username']}:{cisco_device['password']}:{cisco_device['secret']}")
output = connection.send_command('sho arp')
arp_file = f'{prompter[:-1]}_ARP.txt'
with open(arp_file, 'w') as arp:
    arp.write(output)
    print(f'Writing apr {prompter[:-1]} completed successfully')

print('#' * len(output.splitlines()[-1]))
print(output)
print('#' * len(output.splitlines()[-1]))

output1 = connection.send_command('end')
output = connection.send_command('show ip int brief')
ip_int_file = f'{prompter[:-1]}_ip_int.txt'
with open(ip_int_file, 'w') as ip_int:
    ip_int.write(output)
    print(f'Writing apr {prompter[:-1]} completed successfully')

print(output)
print('#' * len(output.splitlines()[-1]))

output = connection.send_command('show run')
show_run_file = f'{prompter[:-1]}show_run.txt'
with open(show_run_file, 'w') as show_run:
    show_run.write(output)
    print(f'Writing apr {prompter[:-1]} completed successfully')

print(output)
print('#' * len(output.splitlines()[-1]))
print(f'Disconnecting from {cisco_device["host"]}')

from netmiko import ConnectHandler
import time

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.88.10',
    'username': 'ross',
    'password': '1212',
    'port': 22,
    'secret': '1212',
    'verbose': True
}
connection = ConnectHandler(**cisco_device)
prompter = connection.find_prompt()
if '>' in prompter:
    connection.enable()

interface = input('Enter interface to enable: ')
output = connection.send_command(f'show interface {interface}')

if 'Invalid input detected at' in output:
    print('#' * 30)
    print('  Invalid interface: ' + interface)
    print('#' * 30)

else:
    int_status = output.splitlines()[0]

    if 'up' in int_status:
        print('#' * 47)
        print("## Interface " + int_status.split()[0] + ' is already enabled' + " ##")
        print('#' * 47)
    else:
        enable_commands = ['conf t', 'interface ' + interface, 'no shut', 'end']
        connection.send_config_set(enable_commands)
        output = connection.send_command(f'show interface {interface}')
        int_status = output.splitlines()[0]
        print('#' * 54)
        print("## Interface " + int_status + "##")
        print('#' * 54)

print('Closing connection')
connection.disconnect()

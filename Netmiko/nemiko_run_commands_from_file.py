from netmiko import ConnectHandler
cisco_device = {
        'device_type': 'cisco_ios',
        'host': '192.168.10.10',
        'username': 'ross',
        'password': '1212',
        'port': 22,
        'secret': '1212',  # this is the enable password
        'verbose': True
    }
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

print('Sending commands from file ...')
output = connection.send_config_from_file('ospf.txt')
print(output)

print('Closing connection')
connection.disconnect()
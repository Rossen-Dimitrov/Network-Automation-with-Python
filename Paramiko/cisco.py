import time
import paramiko
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh_client.connect(
#     hostname='192.168.88.10',
#     port=22, username='ross',
#     password='1212',
#     look_for_keys=False,
#     allow_agent=False
# )
# password = getpass.getpass('Enter password:')

r1 = {'hostname': '192.168.88.10', 'port': 22, 'username': 'ross', 'password': '1212'}
r2 = {'hostname': '192.168.88.20', 'port': 22, 'username': 'ross', 'password': '1212'}
r3 = {'hostname': '192.168.88.30', 'port': 22, 'username': 'ross', 'password': '1212'}
r4 = {'hostname': '192.168.88.40', 'port': 22, 'username': 'ross', 'password': '1212'}
linux = {'hostname': '192.168.88.50', 'port': 22, 'username': 'ross', 'password': '1212'}
routers = [r1, r2, r3, r4]
for router in routers:
    print(f"Connecting to: {router['hostname']}")

    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    shell = ssh_client.invoke_shell()
    shell.send('conf t\n')
    shell.send('ip scp server enable\n')
    shell.send('end\n')
    shell.send('wr\n')
    time.sleep(2)

    output = shell.recv(10000)
    output = output.decode('utf-8')
    print(output)

    if ssh_client.get_transport().is_active():
        ssh_client.close()
        print(f"Closing connection to: {router['hostname']}")

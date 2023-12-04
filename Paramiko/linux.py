import time
import paramiko
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

linux = {'hostname': '192.168.88.50', 'port': 22, 'username': 'ross', 'password': '1212'}

print(f"Connecting to: {linux['hostname']}")

ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('ifconfig\n')
output = stdout.read()
output = output.decode()
print(output)

stdin, stdout, stderr = ssh_client.exec_command('who\n')
time.sleep(0.5)
output = stdout.read()
output = output.decode()
print(output)

stdin, stdout, stderr = ssh_client.exec_command('whossss\n')
output = stdout.read()
output = output.decode()
print(stderr.read().decode())

if ssh_client.get_transport().is_active():
    ssh_client.close()
    print(f"Closing connection to: {linux['hostname']}")

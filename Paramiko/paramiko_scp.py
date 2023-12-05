import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname='192.168.88.50', port=22, username='ross', password='1212',
                   allow_agent=False, look_for_keys=False
                   )
scp = SCPClient(ssh_client.get_transport())

# copy a single file
scp.put('192.168.88.10_2023-12-5.txt', '/tmp/aa.txt')

# copy a directory
scp.put('bkp_directory', recursive=True, remote_path='/tmp')

# copy from remote machine; for windwos - 'C:\\Users\\ad\\file_from-remote_machine.txt'
scp.get('/etc/passwd', 'passwd')

scp.close()




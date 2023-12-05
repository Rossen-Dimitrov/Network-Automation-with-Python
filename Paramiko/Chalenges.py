import myparamiko
import threading
import getpass

commands = [
    'conf t',
    'router rip'
    'version 2',
    'net 10.0.0.0',
    'end',
    'term len 0',
    'sh ip protocols',
    'write',
]
def show_users(router):
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)

    for command in commands:
        myparamiko.send_command(shell, command)

    output = myparamiko.show(shell)
    output_list = output.splitlines()
    output_list = output_list[3:]
    output = '\n'.join(output_list)
    print(output)

    # from datetime import datetime
    # now = datetime.now()
    # year = now.year
    # month = now.month
    # day = now.day
    #
    # file_name = f'{router["server_ip"]}_{year}-{month}-{day}.txt'
    # with open(file_name, 'w') as f:
    #     f.write(output)

    myparamiko.close(client)


# password = getpass.getpass('Enter password:')
router1 = {'server_ip': '192.168.88.10', 'server_port': 22, 'user': 'ross', 'passwd': '1212'}
router2 = {'server_ip': '192.168.88.20', 'server_port': 22, 'user': 'ross', 'passwd': '1212'}
router3 = {'server_ip': '192.168.88.30', 'server_port': 22, 'user': 'ross', 'passwd': '1212'}

routers = [router1, router2, router3]

threads = list()
for router in routers:
    th = threading.Thread(target=show_users, args=(router,))
    threads.append(th)  # appending the thread to the list

for th in threads:
    th.start()

for th in threads:
    th.join()

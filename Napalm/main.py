import json

from napalm import get_network_driver

driver = get_network_driver('ios')
optional_args = {'secret': 'some_pass'} #enable password

ios_router = driver('192.168.88.10', 'ross', '1212', optional_args=optional_args)
ios_router.open()

output = ios_router.get_arp_table()
# for item in output:
#     print(item)

dump = json.dumps(output, indent=4, sort_keys=True)
print(dump)


ios_router.close()

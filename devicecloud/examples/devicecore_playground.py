from devicecloud import DeviceCloud
from getpass import getpass
import pprint
import time


def get_authenticated_dc():
    while True:
        user = raw_input("username: ")
        password = getpass("password: ")
        dc = DeviceCloud(user, password)
        if dc.has_valid_credentials():
            print ("Credentials accepted!")
            return dc
        else:
            print ("Invalid username or password provided, try again")


dc = get_authenticated_dc()
devicecore = dc.get_devicecore_api()

device = devicecore.get_device('00:40:9D:50:B0:EA')
device.add_to_group('grp2')

pprint.pprint(device.get_device_json(use_cached=False))

# device.add_to_group('grp1')
# device.remove_from_group()
# print device.get_group_path()
# print 'done.'
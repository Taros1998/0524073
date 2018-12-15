#!/usr/bin/env python
from __future__ import print_function

import binascii
import pygatt
import time

#YOUR_DEVICE_ADDRESS = "E7:7E:BD:45:22:B2"
device_address = "EB:D0:20:A5:71:6B"
# Many devices, e.g. Fitbit, use random addressing - this is required to
# connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random

def indication_callback(handle, value):
        print("indication, handle %d: %s " % (handle, value))

def device_send():
    adapter = pygatt.GATTToolBackend()
    adapter.start()
    device = adapter.connect(device_address, address_type=ADDRESS_TYPE)


    #for uuid in device.discover_characteristics().keys():
        #print("Read UUID %s: %s" % (uuid, binascii.hexlify(device.char_read(uuid))))

    device.subscribe("6e400002-b5a3-f393-e0a9-e50e24dcca9e", callback=indication_callback, indication=True)
    print("----- device.char_write_handle() -----")
    in_buf = map(ord, "g")
    device.char_write("6e400002-b5a3-f393-e0a9-e50e24dcca9e", in_buf)
    print("Go")
    time.sleep(0.65)
    device.char_write("6e400002-b5a3-f393-e0a9-e50e24dcca9e", map(ord, "n"))
    print("Stop")
    #device.char_write_handle(0x08, in_buf)

if __name__ == '__main__':
    device_send()

import time
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1')
client.connect()
try:
    while True:
        client.write_register(address=512, value=1, unit=1)
        time.sleep(2)
        client.write_register(address=512, value=2, unit=1)
        time.sleep(2)
        print("Cycle Completed")
# result = client.read_holding_registers(address=0, count=1, slave=1) # get information from IO
# print(result) # use information
finally:
    client.close()
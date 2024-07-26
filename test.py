from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1')
client.connect()

try:
    while True:
        result = client.read_holding_registers(address=0, count=1, slave=1) # get information from IO
        print(result) # use information
finally:
    client.close()
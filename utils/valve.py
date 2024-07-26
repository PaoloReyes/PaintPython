from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1')
client.connect()

class Valve:
    def __init__(self, address: int, open_bit: int, close_bit: int):
        self.address = address
        self.open_value = 2**open_bit
        self.close_value = 2**close_bit

    def __get_current_state(self):
        return client.read_holding_registers(address=self.address, count=1, unit=1).registers[0]

    def open(self):
        target_state = (self.__get_current_state() | self.open_value) & ~self.close_value
        client.write_register(address=self.address, value=target_state, unit=1)

    def close(self):
        target_state = (self.__get_current_state() | self.close_value) & ~self.open_value
        client.write_register(address=self.address, value=target_state, unit=1)
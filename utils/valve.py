import time
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1')
client.connect()

class Valve:
    def __init__(self, address: int, open_bit: int, close_bit: int):
        # Modbus Values
        self.address = address
        self.open_value = 2**open_bit
        self.close_value = 2**close_bit

        # Valve Values
        self.__angle = 0.0
        
        # The following values are specific to the valve used in the project
        self.angle_to_time_slope = 41.111
        self.reset_time = 5.0

    def __get_current_state(self):
        return client.read_holding_registers(address=self.address, count=1, unit=1).registers[0]
    
    def __wait(self, time: float):
        time.sleep(time)

    @property
    def angle(self):
        return self.__angle

    def reset(self):
        self.close(self.reset_time)

    def turn_to_angle(self, desired_angle: float):
        time_to_turn = self.__angle_to_time_slope * desired_angle
        if desired_angle - self.__angle > 0:
            self.open(time_to_turn)
        else:
            self.close(time_to_turn)
        self.__angle = desired_angle

    def open(self, time: float):
        target_state = (self.__get_current_state() | self.open_value) & ~self.close_value
        client.write_register(address=self.address, value=target_state, unit=1)
        self.__wait(time)
        self.stop()

    def close(self, time: float):
        target_state = (self.__get_current_state() | self.close_value) & ~self.open_value
        client.write_register(address=self.address, value=target_state, unit=1)
        self.__wait(time)
        self.stop()

    def stop(self):
        target_state = self.__get_current_state() & ~self.open_value & ~self.close_value
        client.write_register(address=self.address, value=target_state, unit=1)
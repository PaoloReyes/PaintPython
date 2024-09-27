# from utils.valve import Valve

# def main():
#     valve = Valve(address=512, open_bit=1, close_bit=0)
#     valve.reset()
#     while True:
#         try:
#             valve_angle = float(input("Desired Angle: "))
#         except ValueError:
#             continue

#         valve.turn_to_angle(valve_angle)

# if __name__ == '__main__':
#     main()

from pymodbus.server.sync import StartSerialServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
import logging

# Configure the logger
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Create a Modbus data store (this simulates the memory of the PLC)
store = ModbusSlaveContext(
    di=None,  # Discrete Inputs
    co=ModbusSlaveContext(coils=[0] * 1000),  # Coils
    hr=ModbusSlaveContext(holding_registers=[0] * 1000),  # Holding Registers
    ir=None  # Input Registers
)

context = ModbusServerContext(slaves=store, single=True)

# Configure the identity of the Modbus server
identity = ModbusDeviceIdentification()
identity.VendorName = 'PLC'
identity.ProductCode = 'PFC200'
identity.VendorUrl = 'http://www.wago.com'
identity.ProductName = 'WAGO PFC200 Modbus RTU Server'
identity.ModelName = 'PFC200'
identity.MajorMinorRevision = '1.0'

# Start the Modbus RTU server on the serial interface
def run_modbus_server():
    StartSerialServer(
        context,
        identity=identity,
        port='/dev/ttyO1',  # Replace with your correct serial port
        baudrate=19200,     # Same baudrate as Arduino
        parity='E',         # Parity setting (8E1 as per Arduino setup)
        stopbits=1,
        bytesize=8
    )

if __name__ == "__main__":
    print("Starting Modbus RTU server...")
    run_modbus_server()
import time
from utils.valve import Valve

def main():
    valve = Valve(address=512, open_bit=0, close_bit=1)
    while True:
        valve.open()
        time.sleep(2)
        valve.close()
        time.sleep(2)

if __name__ == '__main__':
    main()
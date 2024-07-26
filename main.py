from utils.valve import Valve

def main():
    valve = Valve(address=512, open_bit=1, close_bit=0)
    valve.reset()
    while True:
        try:
            valve_angle = float(input("Desired Angle: "))
        except ValueError:
            print("Invalid Input")
            continue

        valve.turn_to_angle(valve_angle)

if __name__ == '__main__':
    main()
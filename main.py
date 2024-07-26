from utils.valve import Valve

def main():
    valve = Valve(address=512, open_bit=0, close_bit=1)
    valve.reset()
    while True:
        try:
            valve_angle = float(input("Current Angle: "))
        except ValueError:
            print("Invalid Input")
            continue

        valve.turn_to_angle(valve_angle)
        print(f"Current Angle: {valve.angle}")
        if input("Continue? (y/n): ") == 'n':
            break

if __name__ == '__main__':
    main()
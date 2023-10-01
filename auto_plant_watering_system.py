import pyfirmata
import time

# Define the Arduino board and port
board = pyfirmata.Arduino('COM4')

# Initialize the digital pin D5
pin_d5 = board.get_pin('d:5:o')

# Initialize the analog pin A1
analog_pin = board.get_pin('a:1:i')

try:
    while True:
        # Read the moisture sensor voltage
        v = analog_pin.read()

        print("Moisture sensor voltage before watering:", v)

        if v > 0.6:  # Adjust this threshold as needed
            print("The plant is thirsty")
            pin_d5.write(1)
            time.sleep(0.5)
            pin_d5.write(0)
            time.sleep(2)
        else:
            print("The plant is fine")

        time.sleep(3600)  # Run code once every hour (24 times a day)

except KeyboardInterrupt:
    board.exit()
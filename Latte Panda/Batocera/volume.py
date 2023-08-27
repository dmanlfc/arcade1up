#!/usr/bin/env python3
import time
import serial
import subprocess

# Ensure PySerial is installed
# Ubuntu: sudo apt install python3-serial
# or pip install pyserial

# Serial port configuration
serial_port = '/dev/ttyACM1'
baud_rate = 57600

# Initialize Serial connection
try:
    arduino = serial.Serial(serial_port, baud_rate)
except Exception as e:
    print("Failed to connect on", serial_port)
    exit(1)

# Mapping of switch states to volume levels
switch_to_volume = {
    'MUTE': 0,
    'MEDIUM': 70,
    'HIGH': 100
}

def set_volume(volume_level):
    subprocess.run(["amixer", "-c", "0", "sset", "Master", f"{volume_level}%"])

try:
    current_volume_state = None

    while True:
        try:
            vol_switch_state = arduino.readline().strip().decode("ASCII")

            if vol_switch_state in switch_to_volume:
                target_volume = switch_to_volume[vol_switch_state]

                if current_volume_state != target_volume:
                    print(f"Switch was set to {vol_switch_state}")
                    set_volume(target_volume)
                    current_volume_state = target_volume
                    time.sleep(1)

        except serial.SerialException:
            print("Serial connection lost")
            break
        except Exception as e:
            print("Error:", e)

except KeyboardInterrupt:
    print("Script terminated by user")
finally:
    arduino.close()

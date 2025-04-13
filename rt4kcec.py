import evdev
from evdev import InputDevice, categorize, ecodes
import serial
import subprocess

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 115200

ser = serial.Serial(
    port=SERIAL_PORT,
    baudrate=BAUD_RATE,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,    # No parity (-parenb)
    stopbits=serial.STOPBITS_ONE
)

devices = [InputDevice(path) for path in evdev.list_devices()]
cec_device = None
for device in devices:
    if "TinyUSB" in device.name:
        cec_device = device
        break

if not cec_device:
    print("CEC_Enabler device not found!")
    exit(1)

state = 0

for event in cec_device.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        if key_event.keystate == key_event.key_down:
            if key_event.keycode == "KEY_UP":
                ser.write(b"remote up\n")
            elif key_event.keycode == "KEY_DOWN":
                ser.write(b"remote down\n")
            elif key_event.keycode == "KEY_RIGHT":
                ser.write(b"remote menu\n")
            elif key_event.keycode == "KEY_F12":
                ser.write(b"remote back\n")
            elif key_event.keycode == "KEY_ENTER":
                ser.write(b"remote ok\n")
            elif key_event.keycode == "KEY_G":
                ser.write(b"remote gain\n")
            elif key_event.keycode == "KEY_P":
                ser.write(b"remote phase\n")
            elif key_event.keycode == "KEY_LEFT":
                if state == 0:
                    ser.write(b"remote pwr\n");
                    state = 1
                elif state == 1:
                    ser.write(b"pwr on\n");
                    state = 0

ser.close()
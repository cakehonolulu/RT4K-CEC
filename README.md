# RT4K-CEC

A repository demonstrating how to control RetroTink 4K devices using HDMI-CEC.

## Materials

To get started, you will need the following:

- **Raspberry Pi**  
  Tested with Raspberry Pi 4, but other models should work as long as the script runs.
  
- **Homemade Pico-CEC**  
  Alternatively, you can use the prebuilt CEC_Enabler from [LazerBear Industries](https://www.laserbear.net/products/cec-enabler).
  
- **1 USB-C OTG Y Cable**  
  Splits into two USB-C ports (one for data, one for power). The MOGOOD brand on Amazon has been tested.
  
- **2 USB-A to USB-C Cables**

---

## Setup Instructions

### Hardware Setup

1. **Connect the OTG Y Splitter**
   Attach the splitter to the RT4K.

2. **Power Connection**
   Connect the USB-C power cable to the power input of the Y splitter.

3. **CEC_Enabler Connection**
   - Attach the CEC_Enabler to the RT4K HDMI output port.  
   - Connect an HDMI cable to the other end of the CEC_Enabler.

4. **Raspberry Pi Connections**
   - Use a USB-C to USB-A cable to connect the USB-C port of the CEC_Enabler to the Raspberry Pi.  
   - Use the second USB-C to USB-A cable to connect the Raspberry Pi to the Y splitter's data input port.

---

### Software Setup

1. **Compile the CEC_Enabler Project**
   Run the following commands to build the project:
   ```bash
   cd RT4K-CEC/
   mkdir build
   cd build
   cmake ..
   make
   ```

2. **Flash the CEC_Enabler**
   - To enter flashing mode, connect the device to your computer while pressing the button on the dongle.
   - Copy the resulting ```CEC_Enabler.uf2``` file to the CEC_Enabler.

3. **Reconnect Everything**
   - Reconnect all hardware components as described in the hardware setup.

4. **Run the Script**
   - Execute the script provided in the repository:

   ```python
   python3 rt4kcec.py
   ```

 Ensure the Raspberry Pi has two cables connected:  
   - One to the CEC_Enabler.  
   - One to the RT4K OTG splitter's data input port.

---

## Controls

Use the remote's DPAD to control the RT4K:

- **Up/Down**: Navigate the RT4K menu.  
- **Left**: Power the RT4K on or off.  
- **Right**: Open the RT4K menu.  
- **Back**: Go back.  
- **Channel Up**: Auto gain.  
- **Channel Down**: Auto phase.

---

## Development

This project is actively exploring ways to overcome the limitation of the CEC_Enabler firmware being in USB "Device" mode instead of "Host" mode. If this limitation can be resolved, it may be possible to eliminate the need for the Raspberry Pi entirely, simplifying the setup and reducing hardware requirements because the CEC_Enabler would also be in charge of sending the serial data to the RT4K.

Contributions, ideas, or suggestions on how to achieve this are welcome. Please feel free to open an issue or submit a pull request if you have a way of doing so!

---

## Notes

- Ensure all connections are secure before powering on the devices.  
- The script assumes the Raspberry Pi is properly configured with Python 3 installed.  
- The Python script (`rt4kcec.py`) can be configured as a systemd service on the Raspberry Pi to run in the background without requiring user interaction. This ensures the script starts automatically on boot.

---
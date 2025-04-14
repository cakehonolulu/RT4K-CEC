# RT4K-CEC

A repository demonstrating how to control RetroTink 4K devices using HDMI-CEC.

## Materials

To get started, you will need the following:

- **Homemade Pico-CEC**  
  Alternatively, you can use the prebuilt CEC_Enabler from [LazerBear Industries](https://www.laserbear.net/products/cec-enabler).
  
- **1 USB-C OTG Y Cable**  
  Splits into two USB-C ports (one for data, one for power). The MOGOOD brand on Amazon has been tested.

- **1 USB-C to USB-C cable**
  To connect the Pico-CEC to the OTG Y cable's data port.

<img width = "33%" src="https://github.com/user-attachments/assets/4530e537-c3c7-48e7-aefb-f1df7ab9ef03">

---

## Setup Instructions

### Hardware Setup

1. **Connect the OTG Y Splitter**
   Attach the splitter to the RT4K.

2. **Power Connection**
   Connect the USB-C power cable to the power input of the Y splitter.

3. **CEC_Enabler Connection**
   - Attach the CEC_Enabler to the RT4K HDMI output port.  
   - Connect the HDMI OUT cable to the other end of the CEC_Enabler.
   - Connect the CEC_Enabler to the OTG Y splicer's data port using the TypeC to TypeC cable.

4. **Profit**

---

### Software Setup

1. **Compile the CEC_Enabler Project**
   Run the following commands to build the project:
   ```bash
   git clone https://github.com/cakehonolulu/RT4K-CEC --recursive
   cd RT4K-CEC/CEC_Enabler
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

4. **Profit**

---

## Controls

Use the remote's DPAD to control the RT4K:

- **Up/Down/Left/Right**: Navigate the RT4K menu.
- **Back**: Go back.
- **Channel Up**: Auto gain.
- **Channel Down**: Auto phase.
- **Double-click (1.25s inbetween) up -> Open menu**
- **Double-click (1.25s inbetween) down -> Power on/off**

---

## Notes

- Ensure all connections are secure before powering on the devices.
- Double-click detection could be much better, sometimes gives up false positives.

---

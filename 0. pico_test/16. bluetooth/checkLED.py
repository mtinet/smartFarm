# Source: electrocredible.com , Language: MicroPython
# Import necessary modules
from machine import Pin
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
import time

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()
# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# Set the debounce time to 0. Used for switch debouncing
debounce_time=0

# Create a Pin object for Pin 0, configure it as an input with a pull-up resistor
pin = Pin(0, Pin.IN, Pin.PULL_UP)

while True:
    # Check if the pin value is 0 and if debounce time has elapsed (more than 300 milliseconds)
    if ((pin.value() is 0) and (time.ticks_ms()-debounce_time) > 300):
        # Check if the BLE connection is established
        if sp.is_connected():
            # Create a message string
            msg="pushbutton pressed\n"
            # Send the message via BLE
            sp.send(msg)
        # Update the debounce time    
        debounce_time=time.ticks_ms()
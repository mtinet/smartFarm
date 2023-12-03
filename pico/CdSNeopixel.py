import array
import time
from machine import Pin, ADC

# Configure the number of WS2812 LEDs.
NUM_LEDS = 16
PIN_NUM = 22
brightness = 0.2

# Set the ADC pin for the light sensor
LIGHT_SENSOR_PIN = 26

# Threshold for turning on the NeoPixel based on light intensity
LIGHT_THRESHOLD = 800

# Flag to track whether the NeoPixel is currently on
neopixel_on = False

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Initialize the light sensor
light_sensor = ADC(Pin(LIGHT_SENSOR_PIN))

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i, c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g << 16) + (r << 8) + b
    sm.put(dimmer_ar, 8)

def pixels_fill(color):
    for i in range(len(ar)):
        ar[i] = (color[1] << 16) + (color[0] << 8) + color[2]

while True:
    # Read the light sensor value
    light_value = light_sensor.read_u16() / 16
    print("Light Sensor Value:", light_value)  # Print the light sensor value to the console

    if light_value > LIGHT_THRESHOLD:
        # Turn on NeoPixel if it's not already on
        if not neopixel_on:
            pixels_fill((255, 255, 255))  # White color
            pixels_show()
            neopixel_on = True
    else:
        # Turn off NeoPixel if it's not already off
        if neopixel_on:
            pixels_fill((0, 0, 0))  # Turn off NeoPixel
            pixels_show()
            neopixel_on = False

    # Sleep for a short time to avoid rapid changes
    time.sleep(0.1)


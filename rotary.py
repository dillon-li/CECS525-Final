from RPi import GPIO
from time import sleep
import uinput

# Define our "keyboard"
device = uinput.Device([
    uinput.KEY_A,
    uinput.KEY_Y
    ])

# Define GPIO pin for our CLK pin of rotary encoder
clk = 11

# Define GPIO pin for our DT pin of rotary encoder
dt = 12

# Set pins to inputs with pulldown resistor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initial state setup
clkLastState = GPIO.input(clk)

# Listen for rotations and do shit
try:
    while True:
        # Get current states
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)

        # Check for rotations
        if clkState != clkLastState:
            if dtState != clkState:
                print("We clockwise bois")
                #sleep(1)
                device.emit_click(uinput.KEY_A)
                device.emit_click(uinput.KEY_Y)
                device.emit_click(uinput.KEY_Y)
            else:
                print("We counterclockwise bois")
                #sleep(1)
                device.emit_click(uinput.KEY_Y)
                device.emit_click(uinput.KEY_Y)
                device.emit_click(uinput.KEY_A)
        clkLastState = clkState # set for next rotation
        sleep(0.01) # Put some slight waiting in there

# Not entirely sure why this is here, but it looks important
finally:
    print("in final")
    GPIO.cleanup()

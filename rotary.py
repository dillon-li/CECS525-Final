from RPi import GPIO
from time import sleep
import uinput

# Define our "keyboard"
device = uinput.Device([
    uinput.KEY_A,
    uinput.KEY_Y,
    uinput.KEY_H,
    uinput.KEY_X,
    uinput.KEY_D,
    uinput.KEY_B,
    uinput.KEY_T
    ])

# Define GPIO pin for our CLK pin of rotary encoder
clk = 11

# Define GPIO pin for our DT pin of rotary encoder
dt = 12

button1 = 16
button2 = 15
button3 = 18

# Set pins to inputs with pulldown resistor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initial state setup
clkLastState = GPIO.input(clk)

# Listen for rotations and do shit
try:
    while True:
        # Get current states
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        b1State = GPIO.input(button1)
        b2State = GPIO.input(button2)
        b3State = GPIO.input(button3)
        # Check for rotations
        # print b1State
        #if not b1State:
            #device.emit_click(uinput.KEY_H)
        if not b1State:
            device.emit_click(uinput.KEY_X)
            device.emit_click(uinput.KEY_D)
            sleep(0.2)
        if not b2State:
            device.emit_click(uinput.KEY_H)
            device.emit_click(uinput.KEY_H)
            sleep(0.2)
        if not b3State:
            device.emit_click(uinput.KEY_B)
            device.emit_click(uinput.KEY_T)
            sleep(0.2)
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

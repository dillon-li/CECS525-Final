from RPi import GPIO
from time import sleep

# Define GPIO pin for our CLK pin of rotary encoder
clk = 11

# Define GPIO pin for our DT pin of rotary encoder
dt = 12

button1 = 16
button2 = 15
button3 = 18
LED = 22

# Set pins to inputs with pulldown resistor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

# Initial state setup
clkLastState = GPIO.input(clk)

#Setup NULL_CHAR and define report function
NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        GPIO.output(LED, True)
        fd.write(report.encode())

# Listen for rotations and do shit
try:
    while True:
        # Get current states
        GPIO.output(LED, False)
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
            write_report(chr(32)+NULL_CHAR+chr(11)+NULL_CHAR*5)
            sleep(0.2)
            write_report(NULL_CHAR*8)
        if not b2State:
            write_report(NULL_CHAR*2+chr(18)+NULL_CHAR*5)
            sleep(0.2)
            write_report(NULL_CHAR*8)
        if not b3State:
            write_report(NULL_CHAR+NULL_CHAR+chr(26)+NULL_CHAR*5)
            sleep(0.2)
            write_report(NULL_CHAR*8)
        if clkState != clkLastState:
            if dtState != clkState:
                #print("We clockwise bois")
                #sleep(1)
                write_report(chr(32)+NULL_CHAR+chr(8)+NULL_CHAR*5)
                write_report(NULL_CHAR*8)

            else:
                #print("We counterclockwise bois")
                #sleep(1)
                write_report(chr(32)+NULL_CHAR+chr(15)+NULL_CHAR*5)
                write_report(NULL_CHAR*8)
        clkLastState = clkState # set for next rotation
        sleep(0.01) # Put some slight waiting in there

# Not entirely sure why this is here, but it looks important
finally:
    print("in final")
    GPIO.cleanup()

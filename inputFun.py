import uinput
from time import sleep

device = uinput.Device([
    uinput.KEY_A,
    uinput.KEY_Y
    ])

sleep(1)
device.emit_click(uinput.KEY_A)
device.emit_click(uinput.KEY_Y)
device.emit_click(uinput.KEY_Y)

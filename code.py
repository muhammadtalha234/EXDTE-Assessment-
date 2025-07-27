import board
import digitalio
import time
import pwmio
import analogio
from adafruit_debouncer import Debouncer
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

button_pin = digitalio.DigitalInOut(board.GP12)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP
my_button = Debouncer(button_pin)


while True:
    if my_button.rose is True:
        print('Just released ')
    if my_button.fell is False:
        print('Just pressed')

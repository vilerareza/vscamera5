import board
import neopixel
import time

class RGBLed():

    pin = board.D10

    def __init__(self) -> None:
        self.color = neopixel.NeoPixel(self.pin, 1)
        self.set_brightness()
        self.set_color((0, 0, 0))

    def set_brightness(self, brightness = 0.1):
        self.color.brightness = brightness

    def set_color(self, color = (0, 0, 0)):
        self.color[0] = color

status_led = RGBLed()
status_led.set_color((0,255,0))
time.sleep(10)
status_led.set_brightness(0)
status_led.set_color()

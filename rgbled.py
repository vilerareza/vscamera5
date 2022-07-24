import board
import neopixel
import time

class RGBLed():

    pin = board.D10

    def __init__(self) -> None:
        self.color = neopixel.NeoPixel(self.pin, 1, brightness = 0.1, auto_write = True)
        #self.set_brightness()
        self.set_color((0, 0, 0))

    def set_brightness(self, brightness = 0.1):
        self.color.brightness = brightness

    def set_color(self, color = (0, 0, 0)):
        self.color[0] = color

status_led = RGBLed()
status_led.set_color((0,255,0))
time.sleep(5)
status_led.color.fill((0,0,0))
time.sleep(5)
status_led.set_color((0,255,0))

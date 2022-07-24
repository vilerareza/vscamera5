import board
import neopixel

class RGBLed():

    pin = board.D10

    def __init__(self) -> None:
        self.color = neopixel.NeoPixel(self.pin, 1)
        self.set_color(0, 0, 0)

    def set_color(self, color = (0, 0, 0)):
        self.color[0] = color

status_led = RGBLed()
status_led.set_color(0,255,0)
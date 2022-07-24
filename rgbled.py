import board
import neopixel

class RGBLed():

    def __init__(self, pin = "D10") -> None:
        self.color = neopixel.NeoPixel(board.pin, 1)
        self.set_color(0, 0, 0)

    def set_color(self, color = (0, 0, 0)):
        self.color[0] = color

status_led = RGBLed()
status_led.set_colot(0,255,0)
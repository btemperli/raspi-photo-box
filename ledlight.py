import board
import neopixel
import time
import global_variables as glv


class LedLight:

    ORDER = neopixel.GRBW
    BRIGHTNESS = 0.2
    NUM_PIXEL = 108

    GREEN = (0, 255, 0, 0)
    BLUE = (0, 0, 255, 0)
    WHITE = (255, 255, 255, 255)
    WHITE2 = (0, 0, 0, 255)
    RED = (255, 0, 0, 0)
    ORANGE = (255, 127, 0, 0)
    YELLOW = (255, 255, 0, 0)
    BLACK = (0, 0, 0)

    def __init__(self):
        self.pixels = neopixel.NeoPixel(
            board.D21,
            self.NUM_PIXEL,
            brightness=self.BRIGHTNESS,
            auto_write=False,
            pixel_order=self.ORDER
        )

        self.show_black()

    def led_show_test(self):
        self.pixels.fill(self.ORANGE)
        self.pixels[0] = self.RED
        self.pixels[23] = self.WHITE2
        self.pixels[24] = self.RED
        self.pixels[18] = self.RED
        self.pixels[19] = self.GREEN
        self.pixels[20] = self.BLUE
        self.pixels[36] = self.WHITE2
        self.pixels[12] = self.WHITE2
        self.pixels[50] = self.BLUE
        self.pixels[102] = self.GREEN
        self.pixels[106] = self.RED
        self.pixels.show()

    def show_green(self):
        self.pixels.fill(self.GREEN)
        self.pixels.show()

    def show_red(self):
        self.pixels.fill(self.RED)
        self.pixels.show()

    def show_black(self):
        self.pixels.fill(self.BLACK)
        self.pixels.show()

    def show_green_time(self, duration):
        self.show_green()
        time.sleep(duration)

    def show_red_time(self, duration):
        self.show_red()
        time.sleep(duration)

    def flash(self):
        self.pixels.brightness = 1
        self.pixels.fill(self.WHITE)
        time.sleep(glv.TIME_FLASH)
        self.pixels.brightness = self.BRIGHTNESS

    def show_turnaround(self, color_background, color_main, led_start, led_stop, turnarounds, delay=0.1):
        for k in range(turnarounds):
            for i in range(led_start, led_stop + 1):
                for j in range(led_start, led_stop + 1):
                    self.pixels[j] = color_background
                self.pixels[i] = color_main
                self.pixels.show()
                time.sleep(delay)

    def turnaround_red_lt(self):
        self.show_turnaround(self.BLACK, self.RED, 0, 23, 1, 0.05)

    def turnaround_red_rt(self):
        self.show_turnaround(self.BLACK, self.RED, 24, 47, 1, 0.05)

    def turnaround_green_lt(self):
        self.show_turnaround(self.BLACK, self.GREEN, 0, 23, 1)

    def turnaround_green_rt(self):
        self.show_turnaround(self.BLACK, self.GREEN, 24, 47, 1)

    def stop(self):
        self.pixels.fill(self.BLACK)
        self.pixels.show()
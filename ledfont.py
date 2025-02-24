import board
import neopixel
import time
import random
import threading
import global_variables as glv


class LedFont:

    INV_ORANGE = (255, 127, 0)
    INV_ORANGE_LIGHT = (255, 127+50, 50)
    INV_YELLOW = (255, 255, 0)
    INV_RED = (255, 0, 0)
    INV_GREEN = (0, 255, 0)
    INV_BLUE = (0, 0, 255)
    INV_CYAN = (0, 255, 255)
    INV_MAGENTA = (255, 0, 255)
    INV_VIOLET = (90, 0, 255)
    INV_BLACK = (0, 0, 0)
    INV_WHITE = (255, 255, 255)

    LED_F_START = 0
    LED_O1_START = 8
    LED_T_START = 16
    LED_O2_START = 23
    LED_S_START = 31
    DURATION = 30

    pixels_font = None
    show_pixels = True
    debug = False

    def __init__(self):
        BRIGHTNESS = 0.5
        self.pixels_font = neopixel.NeoPixel(
            board.D18,
            39,
            brightness=BRIGHTNESS,
            auto_write=False,
            pixel_order=neopixel.RGB
        )

        self.thread_show = None

    def led_show_font_rainbow_slide(self):
        while self.show_pixels:
            colors = [self.INV_RED, self.INV_YELLOW, self.INV_GREEN, self.INV_CYAN, self.INV_BLUE, self.INV_MAGENTA]
            for _ in range(len(colors)):
                for _ in colors:
                    self.colorize_letter_f(colors[0])
                    self.colorize_letter_o1(colors[1])
                    self.colorize_letter_t(colors[2])
                    self.colorize_letter_o2(colors[3])
                    self.colorize_letter_s(colors[4])
                colors.insert(0, colors.pop())
                time.sleep(1)
                if not self.show_pixels:
                    self.stop()
                    break

            self.pixels_font.fill(self.INV_ORANGE)
            self.pixels_font.show()
            time.sleep(1)
            if not self.show_pixels:
                self.stop()

    def led_font_blink_orange(self, duration=16):
        i = 0
        while self.show_pixels and i < duration:
            colors = [self.INV_ORANGE, self.INV_ORANGE_LIGHT, self.INV_ORANGE, self.INV_ORANGE_LIGHT, self.INV_ORANGE]
            for _ in range(len(colors)):
                for _ in colors:
                    self.colorize_letter_f(colors[0])
                    self.colorize_letter_o1(colors[1])
                    self.colorize_letter_t(colors[2])
                    self.colorize_letter_o2(colors[3])
                    self.colorize_letter_s(colors[4])
                colors.insert(0, colors.pop())
                time.sleep(0.25)
                if not self.show_pixels:
                    self.stop()
                    break
            i += 1

    def led_font_single_point(self, duration=DURATION, double=False):
        i = 0
        colorMain = self.INV_ORANGE
        colorDot = self.INV_WHITE
        while self.show_pixels and i < duration:
            dot = 0
            while dot < 39 and self.show_pixels:
                self.pixels_font.fill(colorMain)
                self.pixels_font[dot] = colorDot
                if double:
                    self.pixels_font[38 - dot] = colorDot
                self.pixels_font.show()
                time.sleep(0.0256)
                dot += 1
            i += 1

    def led_font_fill_letters(self, duration, colorStart, colorFill, blink=True):
        i = 0
        while self.show_pixels and i < duration:
            dot = 0
            if not blink:
                colorStart, colorFill = colorFill, colorStart
            while dot < 8 and self.show_pixels:
                self.pixels_font.fill(colorStart)
                if blink:
                    self.pixels_font[self.LED_F_START + dot] = colorFill
                    self.pixels_font[self.LED_O1_START + dot] = colorFill
                    if (dot < 7):
                        self.pixels_font[self.LED_T_START + dot] = colorFill
                    self.pixels_font[self.LED_O2_START + dot] = colorFill
                    self.pixels_font[self.LED_S_START + dot] = colorFill
                else:
                    for k in range(0, dot + 1):
                        self.pixels_font[self.LED_F_START + k] = colorFill
                        self.pixels_font[self.LED_O1_START + k] = colorFill
                        if (k < 7):
                            self.pixels_font[self.LED_T_START + k] = colorFill
                        self.pixels_font[self.LED_O2_START + k] = colorFill
                        self.pixels_font[self.LED_S_START + k] = colorFill
                self.pixels_font.show()
                time.sleep(0.125)
                dot += 1
            i += 1

    def run_show(self):
        possibleFunctions = [
            self.led_font_blink_orange,
            self.show_orange,
            self.show_magenta,
            self.show_violet,
            self.show_orange_light,
            [
                self.led_font_single_point,
                [self.DURATION, True]
            ],
            [
                self.led_font_single_point,
                [self.DURATION, False]
            ],
            [
                self.led_font_fill_letters,
                [self.DURATION * 2, self.INV_ORANGE, self.INV_WHITE, False]
            ],
            [
                self.led_font_fill_letters,
                [self.DURATION * 2, self.INV_ORANGE, self.INV_ORANGE_LIGHT]
            ],
            [
                self.led_font_fill_letters,
                [self.DURATION * 2, self.INV_MAGENTA, self.INV_VIOLET, False]
            ],
            [
                self.led_font_fill_letters,
                [self.DURATION * 2, self.INV_MAGENTA, self.INV_VIOLET]
            ]
        ]

        while self.show_pixels:
            index = random.randint(0, len(possibleFunctions) - 1)
            if self.debug:
                print(index, str(possibleFunctions[index]))
            if (callable(possibleFunctions[index])):
                possibleFunctions[index]()
            else:
                args = possibleFunctions[index][1]
                possibleFunctions[index][0](*args)

    def led_font_show_full_letter(self, color, start, length):
        for i in range(start, start + length):
            self.pixels_font[i] = color
        self.pixels_font.show()

    def colorize_letter_f(self, color):
        self.led_font_show_full_letter(color, self.LED_F_START, 8)

    def colorize_letter_o1(self, color):
        self.led_font_show_full_letter(color, 8, 8)

    def colorize_letter_t(self, color):
        self.led_font_show_full_letter(color, 16, 7)

    def colorize_letter_o2(self, color):
        self.led_font_show_full_letter(color, 23, 8)

    def colorize_letter_s(self, color):
        self.led_font_show_full_letter(color, 31, 8)

    def show(self, color, duration):
        self.pixels_font.fill(color)
        self.pixels_font.show()
        time.sleep(duration)

    def show_orange(self, duration=DURATION):
        self.show(self.INV_ORANGE, duration)

    def show_orange_light(self, duration=DURATION):
        self.show(self.INV_ORANGE_LIGHT, duration)

    def show_magenta(self, duration=DURATION):
        self.show(self.INV_MAGENTA, duration)

    def show_violet(self, duration=DURATION):
        self.show(self.INV_VIOLET, duration)

    def show_green(self, duration=DURATION):
        self.show(self.INV_GREEN, duration)

    def showRed(self, duration=DURATION):
        self.show(self.INV_RED, duration)

    def show_white(self, duration=DURATION):
        self.show(self.INV_WHITE, duration)

    def flash(self):
        self.show_white(glv.TIME_FLASH)

    def start_show(self):
        self.show_pixels = True
        self.thread_show = threading.Thread(target=self.run_show)
        self.thread_show.start()

    def stop(self):
        self.show_pixels = False
        self.pixels_font.fill(self.INV_BLACK)
        self.pixels_font.show()

    def restart_show(self):
        self.start_show()
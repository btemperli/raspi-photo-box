import board
import neopixel
import time
import random

class LedFont():

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

    def ledShowFontRainbowSlide(self):
        while self.show_pixels:
            colors = [self.INV_RED, self.INV_YELLOW, self.INV_GREEN, self.INV_CYAN, self.INV_BLUE, self.INV_MAGENTA]
            for _ in range(len(colors)):
                for _ in colors:
                    self.ledFontF(colors[0])
                    self.ledFontO1(colors[1])
                    self.ledFontT(colors[2])
                    self.ledFontO2(colors[3])
                    self.ledFontS(colors[4])
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

    def ledFontBlinkOrange(self, duration=16):
        i = 0
        while self.show_pixels and i < duration:
            colors = [self.INV_ORANGE, self.INV_ORANGE_LIGHT, self.INV_ORANGE, self.INV_ORANGE_LIGHT, self.INV_ORANGE]
            for _ in range(len(colors)):
                for _ in colors:
                    self.ledFontF(colors[0])
                    self.ledFontO1(colors[1])
                    self.ledFontT(colors[2])
                    self.ledFontO2(colors[3])
                    self.ledFontS(colors[4])
                colors.insert(0, colors.pop())
                time.sleep(0.25)
                if not self.show_pixels:
                    self.stop()
                    break
            i += 1

    def ledFontSinglePoint(self, duration=DURATION, double=False):
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

    def ledFontFillLetters(self, duration, colorStart, colorFill, blink=True):
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


    def ledFontStartShow(self):
        possibleFunctions = [
            self.ledFontBlinkOrange,
            self.showOrange,
            self.showMagenta,
            self.showViolet,
            self.showOrangeLight,
            [
                self.ledFontSinglePoint,
                [self.DURATION, True]
            ],
            [
                self.ledFontSinglePoint,
                [self.DURATION, False]
            ],
            [
                self.ledFontFillLetters,
                [self.DURATION * 2, self.INV_ORANGE, self.INV_WHITE, False]
            ],
            [
                self.ledFontFillLetters,
                [self.DURATION * 2, self.INV_ORANGE, self.INV_ORANGE_LIGHT]
            ],
            [
                self.ledFontFillLetters,
                [self.DURATION * 2, self.INV_MAGENTA, self.INV_VIOLET, False]
            ],
            [
                self.ledFontFillLetters,
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


    def ledFontShowFullLetter(self, color, start, length):
        for i in range(start, start + length):
            self.pixels_font[i] = color
        self.pixels_font.show()


    def ledFontF(self, color):
        self.ledFontShowFullLetter(color, self.LED_F_START, 8)
    def ledFontO1(self, color):
        self.ledFontShowFullLetter(color, 8, 8)
    def ledFontT(self, color):
        self.ledFontShowFullLetter(color, 16, 7)
    def ledFontO2(self, color):
        self.ledFontShowFullLetter(color, 23, 8)
    def ledFontS(self, color):
        self.ledFontShowFullLetter(color, 31, 8)

    def show(self, color, duration):
        self.pixels_font.fill(color)
        self.pixels_font.show()
        time.sleep(duration)

    def showOrange(self, duration=DURATION):
        self.show(self.INV_ORANGE, duration)
    def showOrangeLight(self, duration=DURATION):
        self.show(self.INV_ORANGE_LIGHT, duration)
    def showMagenta(self, duration=DURATION):
        self.show(self.INV_MAGENTA, duration)
    def showViolet(self, duration=DURATION):
        self.show(self.INV_VIOLET, duration)
    def showGreen(self, duration=DURATION):
        self.show(self.INV_GREEN, duration)

    def stop(self):
        self.show_pixels = False
        self.pixels_font.fill(self.INV_BLACK)
        self.pixels_font.show()
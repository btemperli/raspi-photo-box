import board
import neopixel
import time
import gpiozero
import threading
from led_font import LedFont

print("hello world")

ORDER = neopixel.GRBW
BRIGHTNESS = 0.2
NUM_PIXEL = 108
thread_font = None

LED_BIG_RED = gpiozero.PWMLED(13) # red/orange
LED_SM_GREEN = gpiozero.PWMLED(26) # red/violet
LED_SM_RED = gpiozero.PWMLED(19) # red/brown
BUTTON_BIG_RED = gpiozero.Button(6) # green/orange
BUTTON_SM_GREEN = gpiozero.Button(20) # green/violet
BUTTON_SM_RED = gpiozero.Button(16) # green/brown

pixels = neopixel.NeoPixel(board.D21, NUM_PIXEL, brightness=BRIGHTNESS, auto_write=False, pixel_order=neopixel.GRBW)
ledFont = LedFont()

GREEN = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)
WHITE = (255, 255, 255, 255)
WHITE2 = (0, 0, 0, 255)
RED = (255, 0, 0, 0)
ORANGE = (255, 127, 0, 0)
YELLOW = (255, 255, 0, 0)

i = 0
show_pixels = True

def ledShowStart():
    pixels.fill(ORANGE)
    pixels[0] = RED
    pixels[23] = WHITE2
    pixels[24] = RED
    pixels[18] = RED
    pixels[19] = GREEN
    pixels[20] = BLUE
    pixels[36] = WHITE2
    pixels[12] = WHITE2
    pixels[50] = BLUE
    pixels[102] = GREEN
    pixels[106] = RED
    pixels.show()

def fontLedStart():
    global thread_font

    if thread_font:
        ledFont.stop()
        thread_font.join()
    thread_font = threading.Thread(target=ledFont.ledFontStartShow)
    thread_font.start()


def ledShowGreen():
    pixels.fill(GREEN)
    pixels.show()
    ledFont.showGreen(0)

def ledShowTurnaround(color_background, color_main, led_start, led_stop, turnarounds):
    for k in range(turnarounds):
        for i in range(led_start, led_stop + 1):
            for j in range(led_start, led_stop + 1):
                pixels[j] = color_background
            pixels[i] = color_main
            pixels.show()
            time.sleep(0.1)


def button_sm_green_pressed():
    print("gruen gedrueckt")
    thread_left = threading.Thread(target=ledShowTurnaround, args=(ORANGE, GREEN, 0, 23, 2))
    thread_right = threading.Thread(target=ledShowTurnaround, args=(ORANGE, GREEN, 24, 47, 2))
    thread_left.start()
    thread_right.start()
    thread_left.join()
    thread_right.join()
    ledShowStart()

def button_sm_red_pressed():
    print("red gedrueckt")
    thread_left = threading.Thread(target=ledShowTurnaround, args=(BLUE, RED, 0, 23, 2))
    thread_right = threading.Thread(target=ledShowTurnaround, args=(BLUE, RED, 24, 47, 2))
    thread_left.start()
    thread_right.start()
    thread_left.join()
    thread_right.join()
    ledShowStart()

def button_big_red_pressed():
    print("gross rot gedrueckt")
    ledShowGreen();

def button_sm_green_released():
    print("losgelassen: green small")

def button_sm_red_released():
    print("losgelassen: red small")

def button_big_red_released():
    ledShowStart()
    fontLedStart()


BUTTON_SM_GREEN.when_pressed = button_sm_green_pressed
BUTTON_SM_RED.when_pressed = button_sm_red_pressed
BUTTON_BIG_RED.when_pressed = button_big_red_pressed

BUTTON_SM_GREEN.when_released = button_sm_green_released
BUTTON_SM_RED.when_released = button_sm_red_released
BUTTON_BIG_RED.when_released = button_big_red_released

ledShowStart()
fontLedStart()

while show_pixels:
    try:
        # do nothing
        # print(i)
        LED_SM_GREEN.value = 1
        LED_SM_RED.value = 1
        LED_BIG_RED.value = 0
        time.sleep(1)
        LED_SM_GREEN.value = 0
        LED_SM_RED.value = 0
        LED_BIG_RED.value = 1
        time.sleep(1)
        i += 1


    except KeyboardInterrupt:
        show_pixels = False
        print("goodbye")
        ledFont.stop()
        thread_font.join()
        pixels.fill((0, 0, 0, 0))
        pixels.show()
        break
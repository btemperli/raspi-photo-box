import photoboxevents
# import tkinter as tk

DEBUG = True

WINDOW_HEIGHT = 1080 #768
WINDOW_WIDTH = 1920 #1280
CAMERA_HEIGHT = 1440
CAMERA_WIDTH = 2560

PORT_LED_LG_RED = 13 # red/orange
PORT_LED_SM_RED = 19 # red/brown
PORT_LED_SM_GRE = 26 # red/violet
PORT_BUTTON_LG_RED = 6 # green/orange
PORT_BUTTON_SM_RED = 16 # green/brown
PORT_BUTTON_SM_GRE = 20 # green/violet

TIME_BUTTON_PULSE = 1.4
TIME_COUNTDOWN_NUMBER = 2.2
TIME_FLASH = 3

SETUP_RAW = 'SETUP_RAW'
SETUP_WITH_GROVE = 'SETUP_WITH_GROVE'
CURRENT_SETUP = SETUP_RAW

EVENT_RUNNING_PHOTO = False
EVENTS = photoboxevents.PhotoBoxEvents()
last_image = ""

INSTANCE_DISPLAY = None
INSTANCE_LEDFONT = None
INSTANCE_LEDLIGHT = None


def set_setup(setup):
    global CURRENT_SETUP
    CURRENT_SETUP = setup
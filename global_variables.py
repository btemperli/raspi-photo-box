import photoboxevents
# import tkinter as tk

DEBUG = True

WINDOW_HEIGHT = 1080 #768
WINDOW_WIDTH = 1920 #1280
CAMERA_HEIGHT = 1440
CAMERA_WIDTH = 2560

PORT_LED_LG_RED = 13
PORT_LED_SM_RED = 19
PORT_LED_SM_GRE = 26
PORT_BUTTON_LG_RED = 6
PORT_BUTTON_SM_RED = 16
PORT_BUTTON_SM_GRE = 20

SETUP_RAW = 'SETUP_RAW'
SETUP_WITH_GROVE = 'SETUP_WITH_GROVE'
CURRENT_SETUP = SETUP_RAW

take_a_photo_running = False
EVENTS = photoboxevents.PhotoBoxEvents()
last_image = ""

INSTANCE_DISPLAY = None


def set_setup(setup):
    global CURRENT_SETUP
    CURRENT_SETUP = setup
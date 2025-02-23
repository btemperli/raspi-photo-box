import photoboxevents
# import tkinter as tk

WINDOW_HEIGHT = 600 #768
WINDOW_WIDTH = 800 #1280

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


def set_setup(setup):
    global CURRENT_SETUP
    CURRENT_SETUP = setup


def set_pg(pg):
    global PYGAME
    PYGAME = pg

def set_screen(screen):
    global SCREEN
    SCREEN = screen
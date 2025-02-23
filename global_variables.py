import photoboxevents
import tkinter as tk


def set_setup(setup):
    global current_setup

    current_setup = setup


def init_variables():
    global take_a_photo_running
    global events
    global last_image
    global root_window
    global window_height
    global window_width
    global port_button_small_red
    global port_button_small_green
    global port_button_big_red
    global SETUP_WITH_GROVE
    global SETUP_RAW
    global take_a_photo_running
    global events
    global last_image

    root_window = tk.Tk()
    window_height = 768
    window_width = 1280
    port_button_small_red = 1
    port_button_small_green = 2
    port_button_big_red = 3

    SETUP_RAW = 'SETUP_RAW'
    SETUP_WITH_GROVE = 'SETUP_WITH_GROVE'

    take_a_photo_running = False
    events = photoboxevents.PhotoBoxEvents()
    last_image = ""


import photoevents
import tkinter as tk

def init_variables():
    global take_a_photo_running
    global events
    global last_image
    global root_window
    global window_width
    global window_height
    
    take_a_photo_running = False
    events = photoevents.PhotoEvents()
    last_image = ""
    root_window = tk.Tk()
    window_height = 768
    window_width = 1280

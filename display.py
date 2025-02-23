import global_variables as glv
import tkinter as tk
from tkinter import ttk

class Display():

    def __init__(self):
        glv.root_window.title("Countdown und Video-Stream")
        glv.root_window.geometry(str(glv.window_width) + "x" + str(glv.window_height))

        self.label = ttk.Label(glv.root_window, text="", font=("Helvetica", 144))
        self.label.pack(ipadx=200, ipady=100)

        self.show_video = tk.BooleanVar(value=True)

        ttk.Button(glv.root_window, text="Photo aufnehmen!", command=glv.events.take_a_photo).pack()

        self.show_video_stream()

    def update_display(self):
        if self.show_video.get():
            self.show_video_stream()
        else:
            self.start_countdown()

    def show_video_stream(self):
        # In diesem Beispiel wird eine graue Box angezeigt.
        print("todo: show video stream")

    def start_countdown(self):
        self.show_video_stream()  # Zeigen Sie die graue Box an
        glv.root_window.after(1000, self.update_countdown, 3)

    def update_countdown(self, count):
        if count > 0:
            self.label.config(image=None, text="")
            self.label["background"] = "orange"
            self.label.config(width=(glv.window_width / 2))
            self.label.config(text="\n" + str(count) + "\n")
            glv.root_window.after(1000, self.update_countdown, count - 1)
        else:
            self.label.config(text="\n\n\n")
            self.label.config(width=glv.window_width)
            self.label["background"] = "white"
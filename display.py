import global_variables as glv
import pygame
# import tkinter as tk
# from tkinter import ttk


class Display():

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((glv.WINDOW_WIDTH, glv.WINDOW_HEIGHT), pygame.FULLSCREEN)  # Raspberry Pi Touchscreen
        pygame.display.set_caption("Fotobox")
        self.font = pygame.font.Font(None, 80)
        self.clock = pygame.time.Clock()
        self.show_video = True

        glv.set_pg(pygame)
        glv.set_screen(screen)

        # glv.root_window.title("Countdown und Video-Stream")
        # glv.root_window.geometry(str(glv.window_width) + "x" + str(glv.window_height))
        #
        # self.label = ttk.Label(glv.root_window, text="", font=("Helvetica", 144))
        # self.label.pack(ipadx=200, ipady=100)
        #
        # self.show_video = tk.BooleanVar(value=True)
        #
        # ttk.Button(glv.root_window, text="Photo aufnehmen!", command=glv.events.take_a_photo).pack()
        #
        # self.show_video_stream()

    def update_display(self):
        if self.show_video:
            self.show_video_stream()
        else:
            self.start_countdown()

    def show_video_stream(self):
        # In diesem Beispiel wird eine graue Box angezeigt.
        print("todo: show video stream")

    def start_countdown(self):
        print("start countdown")
        self.show_video_stream()  # Zeigen Sie die graue Box an
        # glv.root_window.after(1000, self.update_countdown, 3)

    def update_countdown(self, count):
        print("todo: update countdonw", count)
        # if count > 0:
            # self.label.config(image=None, text="")
            # self.label["background"] = "orange"
            # self.label.config(width=(glv.window_width / 2))
            # self.label.config(text="\n" + str(count) + "\n")
            # glv.root_window.after(1000, self.update_countdown, count - 1)
        # else:
            # self.label.config(text="\n\n\n")
            # self.label.config(width=glv.window_width)
            # self.label["background"] = "white"

    def shut_down(self):
        if glv.DEBUG:
            print("display is shutting down")
        glv.PYGAME.quit()
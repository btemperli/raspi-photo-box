import global_variables as glv
import pygame
# import tkinter as tk
# from tkinter import ttk


class Display():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((glv.WINDOW_WIDTH, glv.WINDOW_HEIGHT), pygame.FULLSCREEN)  # Raspberry Pi Touchscreen
        pygame.display.set_caption("Fotobox")
        self.font = pygame.font.Font(None, 80)
        self.clock = pygame.time.Clock()
        self.show_video = True

        self.stream_frame_width = int(glv.CAMERA_WIDTH * 0.6)
        self.stream_frame_height = int(glv.CAMERA_HEIGHT * 0.6)
        self.stream_frame_tl_x = (glv.WINDOW_WIDTH - self.stream_frame_width) // 2
        self.stream_frame_tl_y = (glv.WINDOW_HEIGHT - self.stream_frame_height) // 2

        self.display_black()

        # glv.set_pg(pygame)
        # glv.set_screen(screen)

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

    def update_video_stream_frame(self, frame):
        frame = pygame.surfarray.make_surface(frame)
        frame = pygame.transform.scale(frame, (self.stream_frame_width, self.stream_frame_height))
        self.screen.blit(frame, (self.stream_frame_tl_x, self.stream_frame_tl_y))
        pygame.display.update()

    def display_image(self, image_name):
        img = pygame.image.load(image_name)
        img = pygame.transform.scale(img, (glv.WINDOW_WIDTH, glv.WINDOW_HEIGHT))
        self.screen.blit(img, (0, 0))
        pygame.display.update()

    def display_black(self):
        self.screen.fill((0, 0, 0))
        pygame.display.update()

    def display_countdown_number(self, number):
        countdown_font = pygame.font.Font(None, 800)

        text = countdown_font.render(str(number), True, (255, 255, 255))
        shadow = countdown_font.render(str(number), True, (0, 0, 0))  # Schwarzer Schatten

        text_x = (glv.WINDOW_WIDTH - text.get_width()) // 2
        text_y = (glv.WINDOW_HEIGHT - text.get_height()) // 2  # Leicht nach oben versetzt

        # Erst Schatten, dann Text für besseren Kontrast
        self.screen.blit(shadow, (text_x + 3, text_y + 3))
        self.screen.blit(text, (text_x, text_y))

        pygame.display.update()

    def check_pygame(self):
        print("check pygame")
        print(pygame)

    def show_video_stream(self):
        # In diesem Beispiel wird eine graue Box angezeigt.
        print("todo: show video stream")

    def start_countdown(self):
        print("start countdown")
        self.show_video_stream()  # Zeigen Sie die graue Box an
        # glv.root_window.after(1000, self.update_countdown, 3)

    # def update_countdown(self, count):
    #     if glv.DEBUG:
    #         print("todo: update countdown", count)
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
        # glv.PYGAME.quit()
        pygame.display.quit()
        pygame.quit()
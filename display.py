import global_variables as glv
import pygame
# import tkinter as tk
# from tkinter import ttk


class Display():

    TURQUOISE = (64, 224, 208)
    DARK_TURQUOISE = (0, 128, 128)
    TEXT_COLOR = (255, 255, 255)
    BACKGROUND = (0, 11, 7)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((glv.WINDOW_WIDTH, glv.WINDOW_HEIGHT), pygame.FULLSCREEN)  # Raspberry Pi Touchscreen
        pygame.display.set_caption("Fotobox")
        self.font = pygame.font.Font(None, 80)
        self.clock = pygame.time.Clock()
        self.show_video = True
        self.video_stream_number = None
        self.output_message = None

        self.stream_frame_width = int(glv.CAMERA_WIDTH * 0.6)
        self.stream_frame_height = int(glv.CAMERA_HEIGHT * 0.6)
        self.stream_frame_tl_x = (glv.WINDOW_WIDTH - self.stream_frame_width) // 2
        self.stream_frame_tl_y = (glv.WINDOW_HEIGHT - self.stream_frame_height) // 2

        self.display_black()

    # def update_display(self):
    #     if self.show_video:
    #         self.show_video_stream()
    #     else:
    #         self.start_countdown()

    def update_video_stream_frame(self, frame):
        frame = pygame.surfarray.make_surface(frame)
        frame = pygame.transform.scale(frame, (self.stream_frame_width, self.stream_frame_height))
        self.screen.blit(frame, (self.stream_frame_tl_x, self.stream_frame_tl_y))

        if self.video_stream_number:
            self.display_countdown_number()

        if self.output_message:
            self.display_output_message()

        pygame.display.update()

    def display_image(self, image_name):
        img = pygame.image.load(image_name)
        img = pygame.transform.scale(img, (glv.WINDOW_WIDTH, glv.WINDOW_HEIGHT))
        self.screen.blit(img, (0, 0))
        pygame.display.update()

    def set_video_stream_number(self, number):
        self.video_stream_number = number

    def reset_video_stream_number(self):
        self.set_video_stream_number(None)

    def set_output_message(self, message):
        self.output_message = message
        self.display_frame_border()
        self.display_output_message()

    def display_output_message(self):
        message_font = pygame.font.Font(None, 60)
        text_outline = message_font.render(self.output_message, True, self.DARK_TURQUOISE)
        text_inner = message_font.render(self.output_message, True, self.TEXT_COLOR)
        padding = 50
        margin_bottom = 50

        outline_rect = text_outline.get_rect()
        box_width = outline_rect.width + padding * 2
        box_height = outline_rect.height + padding * 2

        if self.output_message is None:
            return

        box_x = (glv.WINDOW_WIDTH - box_width) // 2
        box_y = glv.WINDOW_HEIGHT - box_height - margin_bottom
        pygame.draw.rect(self.screen, self.TURQUOISE, pygame.Rect(box_x, box_y, box_width, box_height))

        text_x = box_x + (box_width - outline_rect.width) // 2
        text_y = box_y + (box_height - outline_rect.height) // 2

        # inner_rect = text_inner.get_rect(center=text_outline.get_rect(topleft=outline_pos).center)

        self.screen.blit(text_outline, (text_x + 3, text_y + 3))
        self.screen.blit(text_inner, (text_x, text_y))
        pygame.display.update()

    def display_black(self):
        self.screen.fill(self.BACKGROUND)
        pygame.display.update()

    def display_frame_border(self):
        pygame.draw.rect(self.screen, self.DARK_TURQUOISE, pygame.Rect(0, 0, glv.WINDOW_WIDTH, self.stream_frame_tl_y))
        pygame.draw.rect(self.screen, self.DARK_TURQUOISE, pygame.Rect(0, 0, self.stream_frame_tl_x, glv.WINDOW_HEIGHT))
        pygame.draw.rect(self.screen, self.DARK_TURQUOISE, pygame.Rect(glv.WINDOW_WIDTH - self.stream_frame_tl_x, 0, self.stream_frame_tl_x, glv.WINDOW_HEIGHT))
        pygame.draw.rect(self.screen, self.DARK_TURQUOISE, pygame.Rect(glv.WINDOW_HEIGHT - self.stream_frame_tl_y, 0, glv.WINDOW_WIDTH, self.stream_frame_tl_y))

        pygame.display.update()

    def display_countdown_number(self):
        countdown_font = pygame.font.Font(None, 800)

        if self.video_stream_number is None:
            return

        text = countdown_font.render(str(self.video_stream_number), True, self.TEXT_COLOR)
        shadow = countdown_font.render(str(self.video_stream_number), True, self.DARK_TURQUOISE)  # Schwarzer Schatten

        text_x = (glv.WINDOW_WIDTH - text.get_width()) // 2
        text_y = (glv.WINDOW_HEIGHT - text.get_height()) // 2  # Leicht nach oben versetzt

        # Erst Schatten, dann Text für besseren Kontrast
        self.screen.blit(shadow, (text_x + 3, text_y + 3))
        self.screen.blit(text, (text_x, text_y))

    def check_pygame(self):
        print("check pygame")
        print(pygame)
        print(pygame.version.ver, '//', pygame.version.vernum)

    # def show_video_stream(self):
    #     # In diesem Beispiel wird eine graue Box angezeigt.
    #     print("todo: show video stream")
    #
    # def start_countdown(self):
    #     print("start countdown")
    #     self.show_video_stream()  # Zeigen Sie die graue Box an

    def shut_down(self):
        if glv.DEBUG:
            print("display is shutting down")
        # glv.PYGAME.quit()
        pygame.display.quit()
        pygame.quit()
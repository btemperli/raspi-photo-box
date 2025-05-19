import global_variables as glv
import pygame
# import tkinter as tk
# from tkinter import ttk


class Display():

    TURQUOISE = (64, 224, 208)
    DARK_TURQUOISE = (0, 128, 128)
    RED = (220, 60, 70)
    GREEN = (50, 220, 60)
    TEXT_COLOR = (255, 255, 255)
    BACKGROUND = (0, 50, 40)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((glv.WINDOW_WIDTH, glv.WINDOW_HEIGHT), pygame.FULLSCREEN)  # Raspberry Pi Touchscreen
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Fotobox")
        self.font = pygame.font.Font(None, 80)
        self.clock = pygame.time.Clock()
        self.show_video = True
        self.video_stream_number = None
        self.output_message = None
        self.program_running = True
        self.fullscreen = True

        self.stream_frame_width = int(glv.CAMERA_WIDTH * 0.6)
        self.stream_frame_height = int(glv.CAMERA_HEIGHT * 0.6)
        self.stream_frame_tl_x = (glv.WINDOW_WIDTH - self.stream_frame_width) // 2
        self.stream_frame_tl_y = (glv.WINDOW_HEIGHT - self.stream_frame_height) // 2

        self.register_events()
        self.display_black()

    def update_video_stream_frame(self, frame):
        frame = pygame.surfarray.make_surface(frame)
        frame = pygame.transform.scale(frame, (self.stream_frame_width, self.stream_frame_height))

        if self.program_running:
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

    def display_decision(self):
        font = pygame.font.Font(None, 50)
        padding = 40
        circle_radius = 80
        margin = 100

        # Position für den "löschen"-Button (unten rechts)
        delete_circle_x = glv.WINDOW_WIDTH - margin - circle_radius
        delete_circle_y = glv.WINDOW_HEIGHT - margin - circle_radius

        # Position für den "speichern"-Button (unten links)
        save_circle_x = margin + circle_radius
        save_circle_y = glv.WINDOW_HEIGHT - margin - circle_radius

        # Kreise zeichnen
        pygame.draw.circle(self.screen, self.RED, (delete_circle_x, delete_circle_y), circle_radius)
        pygame.draw.circle(self.screen, self.GREEN, (save_circle_x, save_circle_y), circle_radius)

        # Texte rendern
        delete_text = font.render("löschen", True, self.TEXT_COLOR)
        save_text = font.render("speichern", True, self.TEXT_COLOR)

        # Texte zentriert unter den Kreisen platzieren
        delete_text_rect = delete_text.get_rect(center=(delete_circle_x, delete_circle_y + circle_radius + padding))
        save_text_rect = save_text.get_rect(center=(save_circle_x, save_circle_y + circle_radius + padding))

        # Texte anzeigen
        self.screen.blit(delete_text, delete_text_rect)
        self.screen.blit(save_text, save_text_rect)

        pygame.display.update()

    def set_video_stream_number(self, number):
        self.video_stream_number = number

    def reset_video_stream_number(self):
        self.set_video_stream_number(None)

    def set_output_message(self, message):
        if message == self.output_message:
            return

        self.output_message = message
        self.display_frame_border()
        self.display_output_message(True)

    def register_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.fullscreen:
                    self.screen = pygame.display.set_mode((800, 600))
                    pygame.display.update()
                    self.fullscreen = False
                else:
                    self.screen = pygame.display.set_mode((glv.WINDOW_WIDTH, glv.WINDOW_HEIGHT), pygame.FULLSCREEN)
                    pygame.display.update()
                    self.fullscreen = True

    def display_output_message(self, refresh=False):
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

        self.screen.blit(text_outline, (text_x + 3, text_y + 3))
        self.screen.blit(text_inner, (text_x, text_y))

        if refresh:
            pygame.display.update()

    def display_black(self):
        self.screen.fill(self.BACKGROUND)
        pygame.display.update()

    def display_frame_border(self):
        pygame.draw.rect(self.screen, self.BACKGROUND, pygame.Rect(0, 0, glv.WINDOW_WIDTH, self.stream_frame_tl_y))
        pygame.draw.rect(self.screen, self.BACKGROUND, pygame.Rect(0, 0, self.stream_frame_tl_x, glv.WINDOW_HEIGHT))
        pygame.draw.rect(self.screen, self.BACKGROUND, pygame.Rect(glv.WINDOW_WIDTH - self.stream_frame_tl_x, 0, self.stream_frame_tl_x, glv.WINDOW_HEIGHT))
        pygame.draw.rect(self.screen, self.BACKGROUND, pygame.Rect(0, glv.WINDOW_HEIGHT - self.stream_frame_tl_y, glv.WINDOW_WIDTH, self.stream_frame_tl_y))
        pygame.display.update()

    def display_countdown_number(self):
        countdown_font = pygame.font.Font(None, 800)

        if self.video_stream_number is None:
            return

        text = countdown_font.render(str(self.video_stream_number), True, self.TEXT_COLOR)
        shadow = countdown_font.render(str(self.video_stream_number), True, self.DARK_TURQUOISE)

        text_x = (glv.WINDOW_WIDTH - text.get_width()) // 2
        text_y = (glv.WINDOW_HEIGHT - text.get_height()) // 2

        self.screen.blit(shadow, (text_x + 5, text_y + 5))
        self.screen.blit(text, (text_x, text_y))

    def check_pygame(self):
        print("check pygame")
        print(pygame)
        print(pygame.version.ver, '//', pygame.version.vernum)

    def shut_down(self):
        self.program_running = False

        if glv.DEBUG:
            print("display is shutting down")
        pygame.display.quit()
        pygame.quit()
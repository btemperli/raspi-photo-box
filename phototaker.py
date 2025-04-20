import cv2
import glob
import time
import global_variables as glv
import threading
import numpy as np


class PhotoTaker:
    # camera: Acer GP.OTH11.02M
    # @see https://www.galaxus.ch/de/s1/product/acer-gpoth1102m-360-mpx-webcam-14158650?supplier=406802
    # 3.6MP
    # resolution: 2560 x 1440 px
    camera = cv2.VideoCapture(0)

    img_file_name = 'image'
    img_directory = '/home/photobox/projects/raspi-photo-box/images'
    image = None
    image_ready = False
    video_stream_thread = None
    video_stream_thread_running = False

    camera.set(3, glv.CAMERA_WIDTH * 0.75)  # error when it's set to full size
    camera.set(4, glv.CAMERA_HEIGHT * 0.75)

    # video_width = 1280
    # video_height = 720

    def __init__(self):
        self.show_live_video()

        # bring_image_thread = threading.Thread(target=self.update_video_image)
        # bring_image_thread.start()

    def show_live_video(self):
        self.video_stream_thread_running = True
        self.video_stream_thread = threading.Thread(target=self.stream_video_as_thread)
        self.video_stream_thread.daemon = True
        self.video_stream_thread.start()

    def get_next_image_name(self):
        regex_files = self.img_directory + '/' + self.img_file_name + '_*.jpg'
        all_files = glob.glob(regex_files)
        count_files = len(all_files)

        return self.img_directory + '/' + self.img_file_name + '_' + str(count_files) + '.jpg'

    def stream_video_as_thread(self):
        if glv.DEBUG:
            print("")
            print("pygame is loaded?")
            glv.INSTANCE_DISPLAY.check_pygame()

        glv.INSTANCE_DISPLAY.display_black()

        while self.video_stream_thread_running:
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = np.rot90(frame, 3)
                glv.INSTANCE_DISPLAY.update_video_stream_frame(frame)

        if glv.DEBUG:
            print("video stream has stopped.")

    # def update_video_image(self):
    #     while True:
    #         try:
    #             if self.image_ready:
    #                 cv2.namedWindow("image")
    #                 cv2.imshow('image shot', self.image)
    #                 key = cv2.waitKey(1)
    #         except AttributeError:
    #             print("attribute error")
    #             pass

    def shot(self):
        print("photo aufnehmen start.")
        ret, frame = self.camera.read()
        image_name = self.get_next_image_name()

        if ret:
            self.video_stream_thread_running = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame, 2) # flip image: (3 = rotated 90 to left)
            cv2.imwrite(image_name, frame)
            glv.last_image = image_name

            # Foto anzeigen
            glv.INSTANCE_DISPLAY.display_image(image_name)

            time.sleep(3)  # Kurz anzeigen

        # photo_taken = True
        # led.value = 0
        # cv2.imwrite(image_name, self.image)
        # glv.last_image = image_name

        if glv.DEBUG:
            print("phototaker: end_a_photo.")
        glv.EVENTS.end_a_photo()

    def shut_down(self):
        if glv.DEBUG:
            print("phototaker is shutting down")
        self.camera.release()
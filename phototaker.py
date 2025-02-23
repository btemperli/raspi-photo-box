import cv2
import glob
import time
import global_variables as glv
import threading

class PhotoTaker:
    camera = cv2.VideoCapture(0)
    img_file_name = 'image'
    img_directory = '/home/pi/projects/raspi-photo-box/images'
    image = None
    image_ready = False
    video_width = 1280
    video_height = 720

    def __init__(self):
        video_stream_thread = threading.Thread(target=self.stream_video_as_thread)
        video_stream_thread.daemon = True
        video_stream_thread.start()

        bring_image_thread = threading.Thread(target=self.update_video_image)
        bring_image_thread.start()

    def get_next_image_name(self):
        regex_files = self.img_directory + '/' + self.img_file_name + '_*.jpg'
        all_files = glob.glob(regex_files)
        count_files = len(all_files)

        return self.img_directory + '/' + self.img_file_name + '_' + str(count_files) + '.jpg'

    def stream_video_as_thread(self):
        while True:
            if self.camera.isOpened():
                ret, self.image = self.camera.read()
                self.image_ready = True
            time.sleep(0.01)

    def update_video_image(self):
        while True:
            try:
                if self.image_ready:
                    cv2.namedWindow("image")
                    cv2.imshow('image shot', self.image)
                    key = cv2.waitKey(1)
            except AttributeError:
                print("attribute error")
                pass


    def shot(self):
        print("photo aufnehmen start.")
        image_name = self.get_next_image_name()
        cv2.imwrite(image_name, self.image)
        glv.last_image = image_name
        print("photo aufnehmen stop.")
        glv.events.end_a_photo()
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

    camera.set(3, glv.WINDOW_WIDTH)  # Breite
    camera.set(4, glv.WINDOW_HEIGHT)  # Höhe

    # video_width = 1280
    # video_height = 720

    def __init__(self):
        video_stream_thread = threading.Thread(target=self.stream_video_as_thread)
        video_stream_thread.daemon = True
        video_stream_thread.start()

        # bring_image_thread = threading.Thread(target=self.update_video_image)
        # bring_image_thread.start()

    def get_next_image_name(self):
        regex_files = self.img_directory + '/' + self.img_file_name + '_*.jpg'
        all_files = glob.glob(regex_files)
        count_files = len(all_files)

        return self.img_directory + '/' + self.img_file_name + '_' + str(count_files) + '.jpg'

    def stream_video_as_thread(self):
        while True:
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # frame = np.rot90(frame)  # Falls Kamera verdreht
                frame = glv.PYGAME.surfarray.make_surface(frame)
                frame = glv.PYGAME.transform.scale(frame, (800, 480))
                glv.SCREEN.blit(frame, (0, 0))
            # if self.camera.isOpened():
            #     ret, self.image = self.camera.read()
            #     self.image_ready = True
            # time.sleep(0.01)

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
        ret, frame = self.camera.read()
        image_name = self.get_next_image_name()

        if ret:
            cv2.imwrite(image_name, frame)
            glv.last_image = image_name

            # Foto anzeigen
            img = glv.PYGAME.image.load(image_name)
            img = glv.PYGAME.transform.scale(img, (800, 480))
            glv.SCREEN.blit(img, (0, 0))
            glv.PYGAME.display.update()
            time.sleep(2)  # Kurz anzeigen

        # photo_taken = True
        # led.value = 0

        # cv2.imwrite(image_name, self.image)
        # glv.last_image = image_name
        print("photo aufnehmen stop.")
        glv.events.end_a_photo()

    def shut_down(self):
        if glv.DEBUG:
            print("phototaker is shutting down")
        self.camera.release()
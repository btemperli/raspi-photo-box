import threading
import time

import global_variables as glv


class PhotoUploader:

    def __init__(self):
        self.message_output = None
        self.thread_output = None
        self.thread_upload = None
        self.connection = False

        self.check_connection()

    def output(self):
        if not self.message_output:
            return

        if glv.DEBUG:
            print('output the message: ', self.message_output)

        glv.INSTANCE_DISPLAY.set_output_message(self.message_output)
        time.sleep(20)
        glv.INSTANCE_DISPLAY.set_output_message(None)

    def check_connection(self):
        self.connection = False

    def upload(self):
        self.check_connection()

        if not self.connection:
            self.message_output = "no connection..."
            self.thread_output = threading.Thread(target=self.output)
            self.thread_output.start()

        image = glv.last_image
        print("todo: upload photo (" + glv.last_image + ")")

    def shut_down(self):
        if glv.DEBUG:
            print("PhotoUploader is shutting down")

        if self.thread_upload:
            self.thread_upload.join()

        if self.thread_output:
            self.message_output.join()

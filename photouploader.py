import threading
import time
import requests
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
        time.sleep(10)
        glv.INSTANCE_DISPLAY.set_output_message(None)

    def check_connection(self):
        self.connection = False

    def upload(self):
        self.check_connection()

        if not self.connection:
            self.message_output = "no connection: photo will be uploaded later."
            self.thread_output = threading.Thread(target=self.output)
            self.thread_output.start()

        image_path = glv.last_image
        upload_url = glv.ENV_PHOTOBOX_URL_UPLOAD
        token = glv.ENV_PHOTOBOX_TOKEN

        try:
            with open(image_path, 'rb') as image_file:
                files = {'photo': image_file}
                headers = {'token': token}
                response = requests.post(upload_url, files=files, headers=headers)

            if response.status_code == 200:
                self.message_output = "Photo uploaded!"
            else:
                self.message_output = f"Upload failed, {response.status_code}: {response.text}"

        except Exception as e:
            self.message_output = f"Upload error: {str(e)}"

        self.thread_output = threading.Thread(target=self.output)
        self.thread_output.start()

    def shut_down(self):
        if glv.DEBUG:
            print("PhotoUploader is shutting down")

        if self.thread_upload:
            self.thread_upload.join()

        if self.thread_output:
            self.message_output.join()

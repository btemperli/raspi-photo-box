import threading
import time
import requests
import shutil
import os
import global_variables as glv


class PhotoUploader:

    def __init__(self):
        self.message_output = None
        self.thread_output = None
        self.thread_upload = None
        self.thread_upload_old = None
        self.connection = False
        self.message_upload_success = 'Photo saved & uploaded!'
        self.upload_old_image_thread_running = False

        self.check_connection()

        os.makedirs(glv.DIRECTORY_IMAGES_DELETED, exist_ok=True)
        os.makedirs(glv.DIRECTORY_IMAGES_UPLOAD_LATER, exist_ok=True)

        if self.connection:
            os.makedirs(glv.DIRECTORY_IMAGES_UPLOADED, exist_ok=True)  # Zielordner anlegen, falls nicht vorhanden

    def output(self):
        if not self.message_output:
            return

        if glv.DEBUG:
            print('output the message: ', self.message_output)

        glv.INSTANCE_DISPLAY.set_output_message(self.message_output)
        time.sleep(10)
        glv.INSTANCE_DISPLAY.set_output_message(None)

    def check_connection(self):
        try:
            requests.head(glv.ENV_PHOTOBOX_URL_UPLOAD, timeout=5)
            self.connection = True
            return
        except requests.RequestException:
            self.connection = False

        self.connection = False

    def move_to_trash(self):
        image_path = glv.last_image
        dest_path = os.path.join(glv.DIRECTORY_IMAGES_DELETED, os.path.basename(image_path))
        shutil.move(image_path, dest_path)
        self.message_output = "Photo deleted."
        glv.last_image = None

        self.thread_output = threading.Thread(target=self.output)
        self.thread_output.start()

    def upload_single_image(self, image_path):
        upload_url = glv.ENV_PHOTOBOX_URL_UPLOAD
        token = glv.ENV_PHOTOBOX_TOKEN

        try:
            with open(image_path, 'rb') as image_file:
                files = {'photo': image_file}
                data = {'token': token}
                response = requests.post(upload_url, files=files, data=data)

            if response.status_code == 200:
                dest_path = os.path.join(glv.DIRECTORY_IMAGES_UPLOADED, os.path.basename(image_path))
                shutil.move(image_path, dest_path)

                message = self.message_upload_success
            else:
                message = f"Upload failed, {response.status_code}: {response.text}"

        except Exception as e:
            message = f"Upload error: {str(e)}"

        return message

    def upload(self):
        if glv.last_image is None:
            return

        self.check_connection()
        image_path = glv.last_image

        if not self.connection:
            self.message_output = "no connection: photo will be uploaded later."
            self.thread_output = threading.Thread(target=self.output)
            self.thread_output.start()
            dest_path = os.path.join(glv.DIRECTORY_IMAGES_UPLOAD_LATER, os.path.basename(image_path))
            shutil.move(image_path, dest_path)

        self.message_output = self.upload_single_image(image_path)

        if self.message_output == self.message_upload_success:
            glv.last_image = None

        else:
            dest_path = os.path.join(glv.DIRECTORY_IMAGES_UPLOAD_LATER, os.path.basename(image_path))
            shutil.move(image_path, dest_path)

        self.thread_output = threading.Thread(target=self.output)
        self.thread_output.start()

    def upload_old_images_threaded(self):
        files = [
            f for f in os.listdir(glv.DIRECTORY_IMAGES_UPLOAD_LATER)
            if os.path.isfile(os.path.join(glv.DIRECTORY_IMAGES_UPLOAD_LATER, f)) and
               f.startswith("image_") and f.lower().endswith(".jpg")
        ]
        files.sort()
        if files:
            old_image = os.path.join(glv.DIRECTORY_IMAGES_UPLOAD_LATER, files[0])
            message = self.upload_single_image(old_image)

            if glv.DEBUG:
                print('-----')
                print('old photo uploaded', old_image)
                print(message)
                print('-----')

        self.upload_old_image_thread_running = False

    def upload_old_images(self):
        if not self.connection:
            return

        if self.upload_old_image_thread_running:
            return

        self.upload_old_image_thread_running = True
        self.thread_upload_old = threading.Thread(target=self.upload_old_images_threaded)
        self.thread_upload_old.start()

    def shut_down(self):
        if glv.DEBUG:
            print("PhotoUploader is shutting down")

        if self.thread_upload:
            self.thread_upload.join()

        if self.thread_output:
            self.message_output.join()

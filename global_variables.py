import photoboxevents
import os
from dotenv import load_dotenv

DEBUG = True

WINDOW_HEIGHT = 1080 #768
WINDOW_WIDTH = 1920 #1280
CAMERA_HEIGHT = 1440
CAMERA_WIDTH = 2560

PORT_LED_LG_RED = 13 # red/orange
PORT_LED_SM_RED = 19 # red/brown
PORT_LED_SM_GRE = 26 # red/violet
PORT_BUTTON_LG_RED = 6 # green/orange
PORT_BUTTON_SM_RED = 16 # green/brown
PORT_BUTTON_SM_GRE = 20 # green/violet

TIME_BUTTON_PULSE = 1.4
TIME_COUNTDOWN_NUMBER = 2.2
TIME_FLASH = 3

SETUP_RAW = 'SETUP_RAW'
SETUP_WITH_GROVE = 'SETUP_WITH_GROVE'
CURRENT_SETUP = SETUP_RAW

STAGE_WAITING = 'WAITING'
STAGE_PHOTO_TAKING = 'PHOTO_TAKING'
STAGE_WAIT_FOR_DECISION = 'WAIT_FOR_DECISION'
CURRENT_STAGE = STAGE_WAITING

EVENT_RUNNING_PHOTO = False
EVENTS = photoboxevents.PhotoBoxEvents()
last_image = ""

DIRECTORY_IMAGES_TAKEN = '/home/photobox/projects/raspi-photo-box/images'
DIRECTORY_IMAGES_UPLOAD_LATER = '/home/photobox/projects/raspi-photo-box/upload-later'
DIRECTORY_IMAGES_UPLOADED = '/home/photobox/projects/raspi-photo-box/uploaded'
DIRECTORY_IMAGES_DELETED = '/home/photobox/projects/raspi-photo-box/deleted'

INSTANCE_DISPLAY = None
INSTANCE_LEDFONT = None
INSTANCE_LEDLIGHT = None
INSTANCE_UPLOADER = None

# .env-Variables
load_dotenv()
ENV_PHOTOBOX_TOKEN = os.getenv('PHOTOBOX_TOKEN')
ENV_PHOTOBOX_URL_UPLOAD = os.getenv('PHOTOBOX_URL_UPLOAD')

def set_setup(setup):
    global CURRENT_SETUP
    CURRENT_SETUP = setup
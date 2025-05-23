import time
import random
import keyboard
import global_variables as glv
import phototaker
import ledfont
import ledlight
import buttonhandler
import display
import photouploader


def shut_down():
    display.shut_down()
    photoTaker.shut_down()
    buttonHandler.shut_down()
    ledFont.stop()
    ledLight.stop()

    if glv.DEBUG:
        print("main.py is shutting down")


def restart():
    if glv.DEBUG:
        print("restart: ledfont / start show")
    ledFont.restart_show()
    ledLight.stop()

    if glv.DEBUG:
        print("restart: buttonhandler / start pulsing")
    buttonHandler.start_pulsing()


def reset_photo_taking():
    glv.EVENT_RUNNING_PHOTO = False
    restart()


# load all the other classes
if glv.DEBUG:
    print("(main.py) start initiating display")
display = display.Display()
glv.INSTANCE_DISPLAY = display

if glv.DEBUG:
    print("(main.py) start initiating ledFont")
ledFont = ledfont.LedFont()
glv.INSTANCE_LEDFONT = ledFont

if glv.DEBUG:
    print("(main.py) start initiating ledLight")
ledLight = ledlight.LedLight()
glv.INSTANCE_LEDLIGHT = ledLight

if glv.DEBUG:
    print("(main.py) start initiating buttonHandler")
buttonHandler = buttonhandler.ButtonHandler()

if glv.DEBUG:
    print("(main.py) start initiating photoUploader")
photoUploader = photouploader.PhotoUploader()
glv.INSTANCE_UPLOADER = photoUploader

# needs to be after display
if glv.DEBUG:
    print("(main.py) start initiating photoTaker")
photoTaker = phototaker.PhotoTaker()

print("-------------------------")
print(" welcome to the photobox ")
print("-------------------------")

# global needed variables.
run = True
glv.CURRENT_STAGE = glv.STAGE_WAITING

# events
glv.EVENTS.take_a_photo += ledFont.set_white
glv.EVENTS.take_a_photo += ledLight.flash
glv.EVENTS.take_a_photo += photoTaker.shot

glv.EVENTS.end_a_photo += photoUploader.upload
glv.EVENTS.end_a_photo += reset_photo_taking
glv.EVENTS.end_a_photo += photoTaker.show_live_video

if glv.DEBUG:
    print("all events are registered: ")
    print(' . length of events: ', len(glv.EVENTS))
    for event in glv.EVENTS:
        print(' . event', event.__name__)

# prepare
if (glv.DEBUG):
    print("start running main program")

restart()

while run:
    try:
        time.sleep(0.2)
        if keyboard.is_pressed("q"):
            glv.INSTANCE_DISPLAY.toggle_fullsize()

        if keyboard.is_pressed("esc"):
            print('ESC pressed, exiting')
            run = False
            shut_down()

        if random.randint(0, 10) == 1:
            glv.INSTANCE_UPLOADER.upload_old_images()

    except IOError:
        print('IOError')
        run = False
        shut_down()

    except KeyboardInterrupt:
        print('good bye')
        run = False
        shut_down()

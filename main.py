import phototaker
import time
import global_variables as glv
import ledfont
import ledlight
import buttonhandler
import display


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
    print("todo: upload photo (" + glv.last_image + ")")
    # read last photo from glv.
    # time.sleep(2)

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

# needs to be after display
if glv.DEBUG:
    print("(main.py) start initiating photoTaker")
photoTaker = phototaker.PhotoTaker()

print("-------------------------")
print(" welcome to the photobox ")
print("-------------------------")

# global needed variables.
run = True

# events
glv.EVENTS.take_a_photo += ledFont.set_white
glv.EVENTS.take_a_photo += ledLight.flash
glv.EVENTS.take_a_photo += photoTaker.shot
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
        time.sleep(0.1)

    except IOError:
        print('IOError')
        run = False
        shut_down()

    except KeyboardInterrupt:
        print('good bye')
        run = False
        shut_down()

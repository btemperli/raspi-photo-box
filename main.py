import phototaker
import time
import global_variables as glv
import ledfont
import ledlight
import buttonhandler
import display

# glv.init_variables()


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
    if glv.DEBUG:
        print("restart: buttonhandler / start pulsing")
    buttonHandler.start_pulsing()


def reset_photo_taking():
    print("todo: upload photo (" + glv.last_image + ")")
    # read last photo from glv.
    time.sleep(2)
    glv.take_a_photo_running = False
    restart()


# load all the other classes
display = display.Display()
glv.INSTANCE_DISPLAY = display

ledFont = ledfont.LedFont()
glv.INSTANCE_LEDFONT = ledFont

ledLight = ledlight.LedLight()
glv.INSTANCE_LEDLIGHT = ledLight

buttonHandler = buttonhandler.ButtonHandler()

# needs to be after display
photoTaker = phototaker.PhotoTaker()

print("-------------------------")
print(" welcome to the photobox ")
print("-------------------------")

# global needed variables.
run = True

# events
glv.EVENTS.take_a_photo += photoTaker.shot
glv.EVENTS.end_a_photo += reset_photo_taking

# prepare
if (glv.DEBUG):
    print("start running main program")

restart()

while run:
    try:
        time.sleep(0.1)
        # digitalInputButton = grovepi.digitalRead(buttonPort)

        if False:
            if not glv.take_a_photo_running:
                glv.take_a_photo_running = True
                glv.events.take_a_photo()


    except IOError:
        print('IOError')
        run = False
        shut_down()

    except KeyboardInterrupt:
        print('good bye')
        run = False
        shut_down()

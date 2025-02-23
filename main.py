import phototaker
import time
import global_variables as glv
import ledfont
import buttonhandler
import display

glv.init_variables()


def restart():
    ledFont.ledFontStartShow()

def reset_photo_taking():
    print("todo: upload photo (" + glv.last_image + ")")
    # read last photo from glv.
    time.sleep(2)
    glv.take_a_photo_running = False
    restart()

# other classes
taker = phototaker.PhotoTaker()
ledFont = ledfont.LedFont()
buttonHandler = buttonhandler.ButtonHandler()
display = display.__init__()

print("welcome to the photobox")

# global needed variables.
run = True

# events
glv.EVENTS.take_a_photo += taker.shot
glv.EVENTS.end_a_photo += reset_photo_taking

# prepare
print("start running program.")
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

    except KeyboardInterrupt:
        print('good bye')
        run = False
import phototaker
import display
import time
import grovepi
import global_variables as glv
import tkinter as tk
import threading

glv.init_variables()

def reset_photo_taking():
    print("todo: upload photo (" + glv.last_image + ")")
    # read last photo from glv.
    time.sleep(2)
    glv.take_a_photo_running = False

# other classes
taker = phototaker.PhotoTaker()
display = display.Display()

grovepi.set_bus('RPI_1')
print("welcome to the photobox")

# global needed variables.
buttonPort = 3
run = True

# events
glv.events.take_a_photo += taker.shot
glv.events.end_a_photo += reset_photo_taking

grovepi.pinMode(buttonPort, "INPUT")

print("start running program.")
def checkButtons():
    while run:
        try:
            time.sleep(0.01)
            digitalInputButton = grovepi.digitalRead(buttonPort)
            
            if (digitalInputButton):
                if not glv.take_a_photo_running:
                    glv.take_a_photo_running = True
                    glv.events.take_a_photo()

        except IOError:
            print('IOError')
            run = False

        except KeyboardInterrupt:
            print('good bye')
            run = False

checkButtonsThread = threading.Thread(target=checkButtons)

# display
glv.root_window.mainloop()
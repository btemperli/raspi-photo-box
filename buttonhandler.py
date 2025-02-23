import gpiozero

class ButtonHandler():

    LED_BIG_RED = gpiozero.PWMLED(13) # red/orange
    LED_SM_GREEN = gpiozero.PWMLED(26) # red/violet
    LED_SM_RED = gpiozero.PWMLED(19) # red/brown
    BUTTON_BIG_RED = gpiozero.Button(6) # green/orange
    BUTTON_SM_GREEN = gpiozero.Button(20) # green/violet
    BUTTON_SM_RED = gpiozero.Button(16) # green/brown

    def __init__(self):
        print("todo: install all buttons")
import gpiozero
import threading
import time
import global_variables as glv


class ButtonHandler():

    LED_LG_RED = gpiozero.PWMLED(glv.PORT_LED_LG_RED)
    LED_SM_RED = gpiozero.PWMLED(glv.PORT_LED_SM_RED)
    LED_SM_GRE = gpiozero.PWMLED(glv.PORT_LED_SM_GRE)
    BUTTON_LG_RED = gpiozero.Button(glv.PORT_BUTTON_LG_RED)
    BUTTON_SM_RED = gpiozero.Button(glv.PORT_BUTTON_SM_RED)
    BUTTON_SM_GRE = gpiozero.Button(glv.PORT_BUTTON_SM_GRE)

    def __init__(self):
        print("todo: install all buttons")

        self.BUTTON_SM_GRE.when_pressed = self.btn_sm_gre_pressed
        self.BUTTON_SM_RED.when_pressed = self.btn_sm_red_pressed
        self.BUTTON_LG_RED.when_pressed = self.btn_lg_red_pressed

        self.pulse_buttons_running = None
        self.thread_pulse = None

    def start_countdown(self):
        glv.EVENT_RUNNING_PHOTO = True
        glv.INSTANCE_LEDFONT.stop()

        for i in range(3, 0, -1):
            print('countdown:', i)
            glv.INSTANCE_DISPLAY.display_countdown_number(i)
            thread_font = threading.Thread(target=glv.INSTANCE_LEDFONT.showRed, args=(glv.TIME_COUNTDOWN_NUMBER,))
            thread_left = threading.Thread(target=glv.INSTANCE_LEDLIGHT.turnaround_red_lt)
            thread_right = threading.Thread(target=glv.INSTANCE_LEDLIGHT.turnaround_red_rt)
            thread_font.start()
            thread_left.start()
            thread_right.start()
            thread_font.join()
            thread_left.join()
            thread_right.join()

        glv.EVENTS.take_a_photo()

    def start_pulsing(self):
        self.pulse_buttons_running = True
        self.thread_pulse = threading.Thread(target=self.pulse_buttons)
        self.thread_pulse.start()

    def pulse_buttons(self):
        while self.pulse_buttons_running:
            self.LED_SM_GRE.value = 0.3
            self.LED_SM_RED.value = 0.3
            self.LED_LG_RED.value = 0
            time.sleep(glv.TIME_BUTTON_PULSE)
            self.LED_SM_GRE.value = 0
            self.LED_SM_RED.value = 0
            self.LED_LG_RED.value = 1
            time.sleep(glv.TIME_BUTTON_PULSE)

    def btn_sm_gre_pressed(self):
        if glv.DEBUG:
            print("SM green gedrueckt")

        thread_left = threading.Thread(target=glv.INSTANCE_LEDLIGHT.show_green_time, args=(0.3,))
        thread_left.start()
        thread_left.join()
        glv.INSTANCE_LEDLIGHT.stop()

    def btn_sm_red_pressed(self):
        if glv.DEBUG:
            print("SM red gedrueckt")

        thread_right = threading.Thread(target=glv.INSTANCE_LEDLIGHT.show_red_time, args=(0.3,))
        thread_right.start()
        thread_right.join()
        glv.INSTANCE_LEDLIGHT.stop()

    def btn_lg_red_pressed(self):
        if glv.DEBUG:
            print("LG red gedrueckt")

        self.start_countdown()

    def shut_down(self):
        if glv.DEBUG:
            print("button-handler is shutting down")
        self.pulse_buttons_running = False
        self.LED_SM_GRE.value = 0
        self.LED_SM_RED.value = 0
        self.LED_LG_RED.value = 0

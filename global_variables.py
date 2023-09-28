import photoevents

def init_variables():
    global take_a_photo_running
    global events
    global last_image

    take_a_photo_running = False
    events = photoevents.PhotoEvents()
    last_image = ""

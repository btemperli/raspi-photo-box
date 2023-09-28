import photoevents

def init_variables():
    global take_a_photo_running
    global events

    take_a_photo_running = False
    events = photoevents.PhotoEvents()

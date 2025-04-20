from events import Events


class PhotoBoxEvents(Events):
    __events__ = ('take_a_photo', 'end_a_photo', )
import enum


class PicklableEnum(enum.Enum):
    """ Mixin to customize enums output. """
    def __getstate__(self):
        """ jsonpicles' __getstate__ protocol implementaion."""
        return str(self)



from .documentable import Documentable


class Library(Documentable):

    @staticmethod
    def operations():
        return {}

class LibraryException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(LibraryException, self).__init__(message)
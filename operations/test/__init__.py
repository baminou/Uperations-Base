
from operations.library import Library
from .allo import Allo

class Test(Library):

    @staticmethod
    def name():
        return "test"

    @staticmethod
    def description():
        return "Not description provided"

    def operations(self):
        return {
            'allo': Allo(self)
        }
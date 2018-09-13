
from .listener import Listener

class TestListener2(Listener):

    def handle(self):
        print("This is test2")
        return
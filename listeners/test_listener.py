
from .listener import Listener

class Testlistener(Listener):

    def handle(self):
        print(self._event._name)
        print("This is a test! %s " % (self._event._name))
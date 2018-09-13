
import abc

class Listener:

    def __init__(self, event):
        self._event = event
        return

    @abc.abstractmethod
    def handle(self):
        raise NotImplementedError
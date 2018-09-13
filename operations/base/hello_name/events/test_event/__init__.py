
from operations.event import Event

class TestEvent(Event):

    @staticmethod
    def _name():
        return "EVENTNAME"

    @staticmethod
    def description():
        return "No description provided for EVENTNAME"

    def __init__(self, operation, name):
        super().__init__(operation)
        self._name = name
        return
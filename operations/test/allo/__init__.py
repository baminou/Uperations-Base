
from operation_types.operation import Operation
from operations.event import Event

class Allo(Operation):

    @staticmethod
    def name():
        return "Allo"

    @staticmethod
    def description():
        return "Allo has not been documented yet."

    def _parser(self, main_parser):
        #main_parser.add_argument('first_argument', help="Argparse argument example")
        return

    def _run(self):
        return
        Event.trigger(TestEvent(name="bonjour"))

from operation_types.operation import Operation

class Test(Operation):

    @staticmethod
    def name():
        return "Test"

    @staticmethod
    def description():
        return "Test has not been documented yet."

    def _parser(self, main_parser):
        return

    def _run(self):
        raise NotImplementedError("Test not implemented yet.")
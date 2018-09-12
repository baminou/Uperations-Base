
from operation_types.operation import Operation

class HelloName(Operation):

    @staticmethod
    def name():
        return "hello_name"

    @staticmethod
    def description():
        return "Print hello to any name argument"

    def _parser(self, main_parser):
        main_parser.add_argument('library', help="Name to say hello to.")
        return

    def _run(self):
        print("Hello %s" % (self.args.name))
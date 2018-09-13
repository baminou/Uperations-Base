
from kernel.operation import Operation
from termcolor import colored
import tabulate
import kernel


class Listoperation(Operation):

    @staticmethod
    def name():
        return "list_operation"

    @staticmethod
    def description():
        return "List all operations"

    def _parser(self, main_parser):
        main_parser.add_argument('-l', '--library', dest='library', required=False)
        return

    def _run(self):
        headers = ['Library', 'Command', 'Operation', 'Description']
        data = []
        for library, library_class in kernel.LIBRARIES.items():
            for operation, operation_class in library_class.operations().items():
                data.append([colored(library,'blue'), colored(operation, 'green'), operation_class.name(), operation_class.description()[:50]])
        print(tabulate.tabulate(data,headers))
        return True

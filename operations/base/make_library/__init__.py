
from operation_types.operation import Operation
from termcolor import cprint
import shutil
import os
from ..utils import library_create

class Makelibrary(Operation):

    def _schema(self):
        return {}

    @staticmethod
    def name():
        return "make_library"

    @staticmethod
    def description():
        return "Create a new library for operations"

    def _parser(self, main_parser):
        main_parser.add_argument('name')
        return

    def _run(self):
        library_create(self.args.name,'operations',os.path.join('operations','base','make_library','template'),{'LIBRARYNAME':self.args.name.lower()})
        return True

from operation_types.operation import Operation
import os
import shutil
from operations.library import Library
from operation_types.operation import Operation
import kernel.console

class Publish(Operation):

    @staticmethod
    def name():
        return "Publish"

    @staticmethod
    def description():
        return "Publish resources files under operation"

    def _parser(self, main_parser):
        main_parser.add_argument('library',help="Library containing the operation")
        main_parser.add_argument('operation',help="Library containing the operation")
        return

    def _run(self):
        operation = kernel.console.find_operation(self.args.library, self.args.operation)
        if operation.is_publishable():
            operation.publish(os.path.join('resources',self.args.library,self.args.operation))
            return
        raise Exception("This operation is not publishable")

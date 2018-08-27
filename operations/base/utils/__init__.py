

import os
import shutil
from termcolor import cprint
import tempfile
from contracts import contract
from operations.library import LibraryException

@contract(library_name='str', out_dir='str', library_template_path='str', placeholders='dict', returns='str')
def library_create(library_name, out_dir, library_template_path, placeholders):
    """
    Create a new libary

    Args:
        library_name (str): Name of the library to create
        out_dir (str): Path of the directory where the library is going to be created
        library_template_path (str):
        placeholders (dict): Dictionary having the placeholder has key and the new value as value

    Return:
        str: Path of the newly created library
    """

    if library_exists(library_name, out_dir):
        raise LibraryException("The library "+library_name+" already exists under "+out_dir)

    if not os.path.isdir(out_dir):
        raise FileNotFoundError(out_dir+" does not exist")

    library_new_path = os.path.join(out_dir, str(library_name).lower())
    library_new_init = os.path.join(library_new_path, '__init__.py')
    tmp_dir = os.path.join(tempfile.mkdtemp(),'tmp')
    tmp_init = os.path.join(tmp_dir, '__init__.py')

    shutil.copytree(library_template_path, tmp_dir)
    replace_placeholders_in_file(tmp_init, placeholders)
    shutil.copytree(tmp_dir,library_new_path)
    shutil.rmtree(tmp_dir)

    cprint("Library successfully created under: %s" % library_new_init, 'green')

    return library_new_path

@contract(file_path='str', placeholders='dict')
def replace_placeholders_in_file(file_path, placeholders):
    """
    Replace a dictionary of placeholders in an existing file

    Args:
        file_path (str): Path of the file with the placeholders
        placeholders (dict): Dictionary containing list of placeholders as key, value {PLACEHOLDER: new_value}

    Raises:
        FileNotFoundError: file_path does not exist
        TypeError: file_path is not a string
        TypeError: placeholders is not a dict
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(file_path+" does not exist")

    for key in placeholders:
        with open(file_path, 'r') as f:
            new_text = f.read().replace(key, placeholders[key])

        with open(file_path, 'w') as f:
            f.write(new_text)
    return

@contract(name='str',operations_dir='str', returns='bool')
def library_exists(name, operations_dir):
    """
    Check if a library exists in the specified directory

    Args:
        name: Name of the library to check existence
        operations_dir: Path of the operations directory

    Return:
        bool: True if the library exists, False otherwise

    Raises:
        FileNotFoundError: The operations directory does not exist
    """
    if not os.path.isdir(operations_dir):
        raise FileNotFoundError(operations_dir+" does not exist.")

    library_path = os.path.join(os.getcwd(), operations_dir, name)
    return os.path.isdir(library_path)

from operations.base import Base

LIBRARIES = {
    Base.name(): Base()
}

def find_operation(library, operation):
    for tmp_lib in LIBRARIES:
        if tmp_lib == library:
            for operation in LIBRARIES[tmp_lib].operations():
                if LIBRARIES[tmp_lib].operations()[operation].name() == operation:
                    return LIBRARIES[tmp_lib].operations()[operation]
            raise Exception("The operation %s:%s does not exist. " % (library, operation))
        raise Exception("The libary %s does not exist." % (library))
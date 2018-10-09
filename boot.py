
from uperations.kernel import Kernel
from libraries.uperation_base.uperation_base import Base

def boot():
    Kernel.get_instance().set_libraries({
        Base.name(): Base()
    })

    Kernel.get_instance().set_observers({
    })
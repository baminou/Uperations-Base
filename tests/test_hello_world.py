
import operations.base.helloworld

def test_hello_world_operation():
    operation = operations.base.helloworld.Helloworld()
    assert operation.name() == 'hello_world'
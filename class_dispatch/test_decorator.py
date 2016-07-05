import pytest
import decorators

@decorators.add_actions(parent='endpoints')
class Sample(object):
    def __init__(self):
        pass

def test_add_actions():
    print type(Sample.endpoint_b)
    sample = Sample()
    sample.endpoint_a(None)
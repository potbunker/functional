import re
import os

class Processor(object):

    def __init__(self):
        pass

PYTHON_FILE=re.compile(r'(?<!__init__)\.py$')
DIR=os.path.join(os.path.dirname(__file__), 'endpoints')
modules = map(lambda x: x.rstrip('.py'), filter(lambda x: bool(PYTHON_FILE.search(x)), os.listdir(DIR)))

for module in modules:
    mod = __import__('endpoints.'+ module).__dict__[module]
    import new
    setattr(Processor, mod.__name__.replace('endpoints.', ''), new.instancemethod(mod.execute, None, Processor))

Processor().endpoint_a(None)





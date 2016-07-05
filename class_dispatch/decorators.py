from functools import wraps
import re
import os


def add_actions(parent):
    def decorator(cls):
        PYTHON_FILE=re.compile(r'(?<!__init__)\.py$')
        DIR=os.path.join(os.path.dirname(__file__), parent)
        modules = map(lambda x: x.rstrip('.py'), filter(lambda x: bool(PYTHON_FILE.search(x)), os.listdir(DIR)))
        mod = __import__(parent, globals=globals(), fromlist=modules)

        @wraps(cls)
        def wrapper(*args, **kwargs):
            import new
            for m in modules:
                setattr(cls, m, new.instancemethod(getattr(mod, m).execute, None, cls))
            return cls
        return wrapper()
    return decorator
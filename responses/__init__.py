import fnmatch
import imp
import inspect
import os
import os.path


def load_all():
    cwd = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(cwd):
        if fnmatch.fnmatch(filename, '*.py'):
            if not fnmatch.fnmatch(filename, '__*'):
                abs_path = os.path.join(cwd, filename)
                module_name = inspect.getmodulename(abs_path)
                imp.load_source(module_name, abs_path)

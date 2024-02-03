import importlib
import os


def package_init(file):
    views = [f for f in os.listdir(os.path.dirname(os.path.abspath(file))) if f.endswith(".py") and f != "__init__.py"]
    for view in views:
        importlib.import_module(os.path.dirname(os.path.relpath(file)).split("/")[-1] + "." + view[:-3])
        print('App imported ' + view + ' successfully.')
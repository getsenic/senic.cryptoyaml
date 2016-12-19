import pytest
from os import path


def asset_path(*parts):
    return path.abspath(path.join(path.dirname(__file__), 'tests', 'data', *parts))


@pytest.fixture(scope='session')
def testing():
    """ Returns the `testing` module. """
    from sys import modules
    return modules[__name__]    # `testing.py` has already been imported


@pytest.fixture(scope='session')
def api():
    """ Returns the `api` module. """
    from . import api
    return api

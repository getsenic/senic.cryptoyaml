import pytest
from os import path


@pytest.fixture(scope='function')
def keyfile_path(tmpdir):
    return path.join(tmpdir.strpath, 'secret')


@pytest.fixture(scope='function')
def keyfile(keyfile_path, api):
    return api.generate_key(keyfile_path)

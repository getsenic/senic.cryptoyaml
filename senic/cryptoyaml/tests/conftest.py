from os import path
import pytest


@pytest.fixture(scope='function')
def new_keyfile_path(tmpdir):
    return path.join(tmpdir.strpath, 'secret')


@pytest.fixture(scope='function')
def new_filepath(tmpdir):
    return path.join(tmpdir.strpath, 'settings.yml.aes')


@pytest.fixture(scope='function')
def new_keyfile(new_keyfile_path, api):
    return api.generate_key(new_keyfile_path)


@pytest.fixture(scope='session')
def keyfile_path(testing):
    return testing.asset_path('secret')


@pytest.fixture(scope='session')
def datafile_path(testing):
    return testing.asset_path('settings.yml.aes')


@pytest.fixture(scope='function')
def keyvalue(keyfile_path):
    return open(keyfile_path, 'rb').read()


@pytest.fixture(scope='function')
def keyenv(keyvalue, monkeypatch):
    monkeypatch.setenv('CRYPTOYAML_SECRET', keyvalue.decode('ascii'))


@pytest.fixture(scope='session')
def demo_values(api, testing):
    return api.read_yaml_from_file(testing.asset_path('plaintext.yml'))


@pytest.fixture(scope='function')
def new_settings(api, testing, new_filepath, keyvalue, demo_values):
    return api.CryptoYAML(new_filepath, key=keyvalue)

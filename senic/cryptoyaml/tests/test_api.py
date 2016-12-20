import os
import pytest
import stat


def test_generate_key_permissions(new_keyfile):
    assert stat.S_IMODE(os.stat(new_keyfile).st_mode) == 0o400


def test_parse_plain_yaml(demo_values):
    assert demo_values['bill-to']['family'] == 'Dumars'


def test_init_empty_settings(api, new_settings):
    assert new_settings.data == dict()


def test_replace_settings(api, new_settings, demo_values):
    new_settings.data = demo_values
    new_settings.write()


def test_init_from_existing_with_keyvalue(api, keyvalue, datafile_path):
    existing = api.CryptoYAML(datafile_path, key=keyvalue)
    assert existing.data['bill-to']['family'] == 'Dumars'


def test_init_from_existing_with_keyfile(api, keyfile_path, datafile_path):
    existing = api.CryptoYAML(datafile_path, keyfile=keyfile_path)
    assert existing.data['bill-to']['family'] == 'Dumars'


def test_init_from_existing_with_environment_variable(api, keyenv, datafile_path):
    existing = api.CryptoYAML(datafile_path)
    assert existing.data['bill-to']['family'] == 'Dumars'


def test_init_without_key(api, datafile_path):
    with pytest.raises(api.MissingKeyException):
        api.CryptoYAML(datafile_path)

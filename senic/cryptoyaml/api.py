from os import chmod, path
from cryptography.fernet import Fernet


def generate_key(filepath):
    fs = path.abspath(path.expanduser(filepath))
    with open(fs, 'wb') as outfile:
        outfile.write(Fernet.generate_key())
    chmod(fs, 0o400)
    return fs


class CryptoYAML(object):
    """Represents an encrypted YAML file"""

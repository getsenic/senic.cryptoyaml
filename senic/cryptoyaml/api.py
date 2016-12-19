from os import chmod, environ, path
from cryptography.fernet import Fernet
import yaml


def generate_key(filepath):
    fs = path.abspath(path.expanduser(filepath))
    with open(fs, 'wb') as outfile:
        outfile.write(Fernet.generate_key())
    chmod(fs, 0o400)
    return fs


def read_yaml_from_file(filepath):
    return yaml.load(
        open(filepath, 'rb'))


class CryptoYAML(object):
    """Represents an encrypted YAML file"""

    def __init__(self, filepath, key=None, keyfile=None):
        self.filepath = filepath
        self.key = key
        if self.key is None:
            if keyfile is None:
                self.key = environ.get('CRYPTOYAML_SECRET').encode('utf-8')
            else:
                self.key = open(keyfile, 'rb').read()
        assert self.key is not None
        self.fernet = Fernet(self.key)
        self.read()

    def read(self):
        """ Reads and decrypts data from the filesystem """
        if path.exists(self.filepath):
            with open(self.filepath, 'rb') as infile:
                self.data = yaml.load(
                    self.fernet.decrypt(infile.read()))
        else:
            self.data = dict()

    def write(self):
        """ Encrypts and writes the current state back onto the filesystem """
        with open(self.filepath, 'wb') as outfile:
            outfile.write(
                self.fernet.encrypt(
                    yaml.dump(self.data, encoding='utf-8')))

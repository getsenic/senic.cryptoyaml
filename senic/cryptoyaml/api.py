from os import chmod, environ, path
from cryptography.fernet import Fernet
import yaml


def generate_key(filepath):
    ''' generates a new, random secret key at the given location on the
    filesystem and returns its path
    '''
    fs = path.abspath(path.expanduser(filepath))
    with open(fs, 'wb') as outfile:
        outfile.write(Fernet.generate_key())
    chmod(fs, 0o400)
    return fs


def read_yaml_from_file(filepath):
    return yaml.load(
        open(filepath, 'rb'))


def get_key(key=None, keyfile=None):
    """ returns a key given either its value, a path to it on the filesystem
    or as last resort it checks the environment variable CRYPTOYAML_SECRET
    """
    if key is None:
        if keyfile is None:
            key = environ.get('CRYPTOYAML_SECRET')
            if key is None:
                raise MissingKeyException(
                    '''You must either provide a key value,'''
                    ''' a path to a key or its value via the environment variable '''
                    ''' CRYPTOYAML_SECRET'''
                )
            else:
                key = key.encode('utf-8')
        else:
            key = open(keyfile, 'rb').read()
    return key


class MissingKeyException(Exception):

    def __init__(self, msg):
        self.msg = msg


class CryptoYAML(object):
    """Represents an encrypted YAML file"""

    def __init__(self, filepath, key=None, keyfile=None):
        self.filepath = path.abspath(path.expanduser(filepath))
        self.key = get_key(key, keyfile)
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

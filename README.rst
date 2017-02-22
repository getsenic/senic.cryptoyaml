senic.cryptoyaml
================

.. image:: https://travis-ci.org/getsenic/senic.cryptoyaml.svg?branch=master
    :target: https://travis-ci.org/getsenic/senic.cryptoyaml

`cryptoyaml` is a python library to manage encrypted YAML files, its motivation was to provide an API for applications to read (and write) potentially sensitive configuration settings (i.e. passwords, personal user information) in encrypted form.

Another motivation is that even in scenarios where the private key to access those settings is persisted alongside the settings themselves, the advantage would be that it becomes trivial to delete those settings securely: you now only need to destroy the key properly and not worry that you leave sensitive bits and bytes on the storage device.


This package is simply a convenience wrapper tailored to that use case. The actual heavy lifting of parsing and writing YAML and encrypting and decrypting it is done by the excellent libraries `PyYAML <http://pyyaml.org>`__ and `cryptography <https://cryptography.io/en/latest/>`__ respectively.
Also, while they support both Python 2.x and 3.x this package only targets Python >= 3.5 (because it's 2016).


API Usage
---------

Here's a simple example::

    >>> from cryptoyaml import generate_key, CryptoYAML
    >>> new_key = generate_key('secret')
    >>> config = CryptoYAML('/path/to/settings.yml.aes', keyfile=new_key)

Initially you must generate a key (it uses the `Fernet symmetric encryption <https://cryptography.io/en/latest/fernet/>`_ from the `cryptography <https://cryptography.io/en/latest/>`__ library) and use it to construct an CryptoYAML instance.

That instance then provides a `data` attribute which is initally an empty dictionary that you can fill with arbitrary data, provided, the `PyYAML <http://pyyaml.org/>`__ library can encode it::

    >>> config.data['foo'] = 123

Note, however, that the data is only persisted on the filesystem when you explicitly commit it to disk like so::

    >>> config.write()

Once written, the file can be re-read as long as the original secret is still provided::

    >>> reread = CryptoYAML('/path/to/settings.yml.aes', keyfile=new_key)
    >>> reread.data['foo']
    >>> 123


Command Line Usage
------------------

Having an encrypted settings file is neat, but sometimes you might want to take a look at it or manipulate it from the command line instead of programmatically.

For this ``cryptoyaml`` has three commands for generating a key, creating a new file, reading it and setting individual settings::

    # cryptoyaml generate_key mysecret
    Created new private key at /Users/senic/Development/senic.cryptoyaml/mysecret
    # cryptoyaml create mysettings.yml.aes --keyfile mysecret
    created new file at /Users/senic/Development/senic.cryptoyaml/mysettings.yml.aes
    # cryptoyaml set mysettings.yml.aes foo bar --keyfile mysecret
    foo -> bar
    # cryptoyaml cat mysettings.yml.aes --keyfile mysecret
    {'foo': 'bar'}



Environment variables
---------------------

A common practice is to provide the secret key via an environment variable.
Simply setting ``CRYPTOYAML_SECRET`` will allow you to omit the key for both API usage and for the command line.

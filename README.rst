senic.cryptoyaml
================

.. image:: https://travis-ci.org/getsenic/senic.cryptoyaml.svg?branch=master
    :target: https://travis-ci.org/getsenic/senic.cryptoyaml

`senic.cryptoyaml` is a python library to manage encrypted YAML files, its motivation was to provide an API for applications to read (and write) potentially sensitive configuration settings (i.e. passwords, personal user information) in encrypted form.

Another motivation is that even in scenarios where the private key to access those settings is persisted alongside the settings themselves, the advantage would be that it becomes trivial to delete those settings securely: you now only need to destroy the key properly and not worry that you leave sensitive bits and bytes on the storage device.


This package is simply a convenience wrapper tailored to that use case. The actual heavy lifting of parsing and writing YAML and encrypting and decrypting it is done by the excellent libraries `ruamel.yaml <http://yaml.readthedocs.io/en/latest/index.html>`_ and `cryptography <https://cryptography.io/en/latest/>`_ respectively.
Also, while they support both Python 2.x and 3.x this package only targets Python >= 3.5.

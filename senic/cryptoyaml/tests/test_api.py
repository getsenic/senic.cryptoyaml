import os
import stat


def test_generate_key_permissions(keyfile):
    assert stat.S_IMODE(os.stat(keyfile).st_mode) == 0o400

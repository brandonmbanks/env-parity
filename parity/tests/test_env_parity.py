from parity.cli import read_keys


class TestEnvParity(object):
    def test_it_reads_keys(self):
        keys = read_keys('./parity/tests/env_files/.test_1.env')
        assert ['KEY1'] == keys

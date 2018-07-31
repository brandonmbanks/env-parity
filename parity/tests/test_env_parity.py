from parity.cli import read_keys, discover_env_files


class TestEnvParity(object):
    def test_it_reads_keys(self):
        keys = read_keys('./parity/tests/env_files/.test_1.env')
        assert ['KEY1'] == keys

    def test_it_discovers_env_files(self):
        file_paths = discover_env_files('./parity/tests/env_files')
        assert [
            './parity/tests/env_files/.test_2.env',
            './parity/tests/env_files/.test_1.env'
        ] == file_paths

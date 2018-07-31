import os
from typing import List


def discover_env_files(dir_path: str) -> List[str]:
    env_file_paths = []
    for file in os.scandir(dir_path):
        if file.is_file():
            if '.env' in file.path:
                env_file_paths.append(file.path)
    return env_file_paths


def read_keys(file_path: str) -> List[str]:
    f = open(file_path, 'r', encoding='utf-8')
    return list(map(lambda x: x.split('=')[0], list(f)))


def main():
    dir_path = './'
    env_file_paths = discover_env_files(dir_path)
    all_keys = []
    for path in env_file_paths:
        keys = read_keys(path)
        if len(all_keys) == 0:
            all_keys = keys
        diff = list(set(keys).symmetric_difference(set(all_keys)))
        if len(diff) > 0:
            for key in diff:
                if key in keys:
                    print('extra {} key in {}'.format(key, path))
                else:
                    print('missing {} key in {}'.format(key, path))

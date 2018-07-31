import os


def read_keys(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    keys = []
    for line in list(f):
        keys.append(line.split('=')[0])
    return keys


def main():
    path = './'
    env_file_paths = []
    for file in os.scandir(path):
        if file.is_file():
            if '.env' in file.path:
                env_file_paths.append(file.path)

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

import os


def main():
    path = './'
    env_file_paths = []
    for file in os.scandir(path):
        if file.is_file():
            if '.env' in file.path:
                env_file_paths.append(file.path)
    for path in env_file_paths:
        f = open(path, 'r', encoding='utf-8')
        keys = []
        for line in list(f):
            keys.append(line.split('=')[0])
    print(keys)

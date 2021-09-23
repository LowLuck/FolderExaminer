import os


def size_in_folder(start_path):
    s = []
    for j in os.listdir(start_path):
        s.append((get_size(f'{start_path}\\{j}'), j))
    return sorted(s, key=lambda x: -x[0])


def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return round(total_size / 1073741824, 3)


# print(size_in_folder(r'C:\Users\LowLu\AppData\Roaming'))

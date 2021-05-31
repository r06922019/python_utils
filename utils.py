import os

def get_all_file_paths(dir_name):
    ret = []
    for parent_dir, sub_dirs, filenames in os.walk(dir_name):
        for filename in filenames:
            ret.append(os.path.join(parent_dir, filename))
    return ret

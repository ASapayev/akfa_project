import os

def create_folder(parent_dir,directory):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)



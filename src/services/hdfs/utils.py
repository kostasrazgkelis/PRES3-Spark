from os.path import join, isdir, isfile
from os import remove, rmdir, listdir
import pandas as pd
from settings import ALLOWED_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_data_from_file(directory: str, filename: str) -> dict:
    columns = pd.read_csv(join(directory, filename), index_col=0, nrows=0).columns.tolist()

    return {'name': filename,
            'columns': columns}


def delete_file(path):
    if isdir(path):
        for file_name in listdir(path):
            # construct full file path
            file = join(path, file_name)
            if isfile(file):
                print('Deleting file:', file)
                remove(file)
        rmdir(path)

    elif isfile(path):
        remove(path)


def choose_file(path):
    if isdir(path):
        return [join(path, file_name) for file_name in listdir(path)][0]

    if isfile(path):
        return path

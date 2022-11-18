from os.path import join, isdir, isfile
from os import remove, rmdir, listdir
import pandas as pd
from settings import ALLOWED_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_data_from_file(directory: str, filename) -> dict:
    result_dict = {'name': None,
                   'columns': [None]}

    df = pd.read_csv(join(directory, filename), header=0)
    columns = df.columns.values.tolist()

    result_dict['name'] = filename
    result_dict['columns'] = columns
    return result_dict


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

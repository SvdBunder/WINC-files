__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os, shutil, fileinput
from zipfile import ZipFile


# assignment Files - part 1


def clean_cache():
    folder_name = "cache"
    if os.path.isdir(folder_name) == True:
        cache_location = os.getcwd() + "\\" + folder_name
        for files in os.listdir(cache_location):
            os.remove(os.path.join(cache_location, files))
    else:
        os.mkdir(folder_name)


# assignment Files - part 2


def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()

    with ZipFile(zip_file_path, mode="r") as zipped_file:
        zipped_file.extractall(cache_dir_path)


# assignment Files - part 3


def cached_files():
    cache_location = os.listdir(os.path.abspath("cache"))
    file_list = []
    for file in cache_location:
        file_list.append(os.path.abspath("cache") + "\\" + file)
    return file_list


# assignment Files - part 4


def find_password(file_list):
    for line in fileinput.input(file_list):
        if "password" in line:
            return line
